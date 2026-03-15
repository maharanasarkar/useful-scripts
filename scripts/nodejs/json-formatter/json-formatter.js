#!/usr/bin/env node

const { program } = require('commander');
const fs = require('fs');
const path = require('path');

const PACKAGE = require('./package.json');

function sortKeys(obj) {
    if (Array.isArray(obj)) {
        return obj.map(sortKeys);
    }
    if (obj !== null && typeof obj === 'object') {
        return Object.keys(obj).sort().reduce((result, key) => {
            result[key] = sortKeys(obj[key]);
            return result;
        }, {});
    }
    return obj;
}

function formatJSON(input, options = {}) {
    let data;
    
    try {
        data = JSON.parse(input);
    } catch (error) {
        throw new Error(`Invalid JSON: ${error.message}`);
    }
    
    if (options.sort) {
        data = sortKeys(data);
    }
    
    if (options.minify || options.compact) {
        return JSON.stringify(data);
    }
    
    return JSON.stringify(data, null, options.indent || 2);
}

function validateJSON(input) {
    try {
        JSON.parse(input);
        return { valid: true, error: null };
    } catch (error) {
        return { valid: false, error: error.message };
    }
}

function readInput(source) {
    if (source === '-') {
        return new Promise((resolve, reject) => {
            let data = '';
            process.stdin.setEncoding('utf8');
            process.stdin.on('data', chunk => data += chunk);
            process.stdin.on('end', () => resolve(data));
            process.stdin.on('error', reject);
        });
    }
    return fs.promises.readFile(source, 'utf8');
}

async function main() {
    program
        .name('json-formatter')
        .description('Format, validate, and prettify JSON files')
        .version(PACKAGE.version)
        .option('-o, --output <file>', 'Output file path (default: stdout)')
        .option('-i, --indent <number>', 'Indentation spaces', '2')
        .option('-s, --sort', 'Sort object keys alphabetically')
        .option('-m, --minify', 'Minify output')
        .option('--compact', 'Compact output (no whitespace)')
        .option('-v, --validate', 'Validate only, no output')
        .option('--stdin', 'Read from stdin')
        .argument('[input]', 'Input JSON file')
        .action(async (input, options) => {
            try {
                let jsonString;
                
                if (options.stdin) {
                    jsonString = await readInput('-');
                } else if (input) {
                    jsonString = await readInput(input);
                } else {
                    console.error('Error: Please provide an input file or use --stdin');
                    process.exit(1);
                }
                
                if (options.validate) {
                    const result = validateJSON(jsonString);
                    if (result.valid) {
                        console.log('Valid JSON');
                        process.exit(0);
                    } else {
                        console.error(`Invalid JSON: ${result.error}`);
                        process.exit(1);
                    }
                }
                
                const formatted = formatJSON(jsonString, {
                    indent: parseInt(options.indent),
                    sort: options.sort,
                    minify: options.minify,
                    compact: options.compact
                });
                
                if (options.output) {
                    await fs.promises.writeFile(options.output, formatted, 'utf8');
                    console.log(`Formatted JSON saved to: ${options.output}`);
                } else {
                    console.log(formatted);
                }
                
            } catch (error) {
                console.error(`Error: ${error.message}`);
                process.exit(1);
            }
        });
    
    await program.parseAsync(process.argv);
}

main();
