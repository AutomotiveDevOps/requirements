#!/bin/bash

# Fix multiple blank lines in .sdoc files
# Ensure exactly one blank line after TITLE in document header

set -e

echo "=== Fixing Blank Lines ==="
echo "Ensuring proper blank line spacing..."
echo

SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

for file in $SDOC_FILES; do
    echo "Fixing: $file ..."
    temp_file=$(mktemp)
    
    in_header=0
    title_found=0
    
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Remove trailing spaces
        line=$(echo "$line" | sed 's/[[:space:]]*$//')
        
        # Handle document header
        if [[ "$line" =~ ^\[DOCUMENT\]$ ]]; then
            in_header=1
            title_found=0
            echo "$line" >> "$temp_file"
            continue
        fi
        
        if [[ $in_header -eq 1 && "$line" =~ ^TITLE: ]]; then
            echo "$line" >> "$temp_file"
            title_found=1
            continue
        fi
        
        # After TITLE in header, add exactly one blank line
        if [[ $title_found -eq 1 && -z "$line" ]]; then
            echo "" >> "$temp_file"
            in_header=0
            title_found=0
            continue
        fi
        
        # Skip multiple blank lines after TITLE
        if [[ $title_found -eq 1 ]]; then
            in_header=0
            title_found=0
        fi
        
        # Write the line
        echo "$line" >> "$temp_file"
    done < "$file"
    
    mv "$temp_file" "$file"
done

echo "✓ All .sdoc files fixed!" 