#!/usr/bin/env bash

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
VERSION="1.0.0"

NUM_RESULTS=10
SORT_BY="size"
REVERSE=false
TARGET_DIR="."

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS] [DIRECTORY]

Analyze and display file sizes in a directory.

OPTIONS:
    -h, --help          Show this help message
    -n, --number NUM    Number of results to show (default: 10)
    -s, --sort SORT     Sort by: size, name, or date (default: size)
    -r, --reverse       Reverse the sort order
    -v, --version       Show version information

ARGUMENTS:
    DIRECTORY           Directory to analyze (default: current directory)

EXAMPLES:
    $SCRIPT_NAME
    $SCRIPT_NAME /path/to/directory
    $SCRIPT_NAME -n 20 /home/user
    $SCRIPT_NAME -s name -r

EOF
    exit 1
}

version() {
    echo "$SCRIPT_NAME version $VERSION"
    exit 0
}

human_readable_size() {
    local size="$1"
    local units=("B" "K" "M" "G" "T" "P")
    local unit_index=0
    
    while (( $(echo "$size >= 1024" | bc -l 2>/dev/null || echo "0") )) && [ $unit_index -lt 5 ]; do
        size=$(echo "scale=2; $size / 1024" | bc)
        ((unit_index++))
    done
    
    echo "${size}${units[$unit_index]}"
}

analyze_directory() {
    local dir="$1"
    local num="$2"
    local sort_by="$3"
    local reverse="$4"
    
    if [ ! -d "$dir" ]; then
        echo "Error: Directory '$dir' does not exist" >&2
        exit 1
    fi
    
    echo "Analyzing: $dir"
    echo ""
    
    local total_files
    total_files=$(find "$dir" -type f 2>/dev/null | wc -l)
    echo "Total files: $(printf "%',d" "$total_files")"
    echo ""
    
    local sort_param
    case "$sort_by" in
        size)
            sort_param="-k5,5n"
            ;;
        name)
            sort_param="-k9,9"
            ;;
        date)
            sort_param="-k6,6M -k7,7n -k8,8n"
            ;;
        *)
            sort_param="-k5,5n"
            ;;
    esac
    
    if [ "$reverse" = "true" ]; then
        sort_param="$sort_param -r"
    fi
    
    echo "Top $num largest files:"
    echo ""
    
    find "$dir" -type f -exec ls -lh {} \; 2>/dev/null | \
        awk '{print $5, $9}' | \
        sort $sort_param | \
        head -n "$num" | \
        nl -w3 -s'. '
}

main() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                ;;
            -v|--version)
                version
                ;;
            -n|--number)
                NUM_RESULTS="$2"
                shift 2
                ;;
            -s|--sort)
                SORT_BY="$2"
                shift 2
                ;;
            -r|--reverse)
                REVERSE=true
                shift
                ;;
            -*)
                echo "Unknown option: $1"
                usage
                ;;
            *)
                TARGET_DIR="$1"
                shift
                ;;
        esac
    done
    
    if ! [[ "$NUM_RESULTS" =~ ^[0-9]+$ ]]; then
        echo "Error: Number must be a positive integer" >&2
        exit 1
    fi
    
    analyze_directory "$TARGET_DIR" "$NUM_RESULTS" "$SORT_BY" "$REVERSE"
}

main "$@"
