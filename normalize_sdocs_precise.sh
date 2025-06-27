#!/bin/bash

# Precise normalization of .sdoc files according to StrictDoc grammar
# This script ensures exactly one blank line after each structural element

set -e

echo "=== Precise StrictDoc Normalization ==="
echo "Applying exact StrictDoc grammar formatting..."
echo

# Find all .sdoc files
SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

TOTAL_FILES=0
NORMALIZED_COUNT=0
ALREADY_CORRECT=0

# Process each file
for file in $SDOC_FILES; do
    TOTAL_FILES=$((TOTAL_FILES + 1))
    echo -n "[$TOTAL_FILES] Normalizing: $file ... "
    
    # Create a temporary file
    temp_file=$(mktemp)
    
    # Read the file and normalize it precisely
    while IFS= read -r line; do
        # Skip empty lines - we'll add them back precisely
        if [[ -z "$line" ]]; then
            continue
        fi
        
        # Add the current line
        echo "$line" >> "$temp_file"
        
        # Add exactly one blank line after specific patterns
        if [[ "$line" =~ ^TITLE:\ .*$ ]]; then
            # Add blank line after TITLE in document header
            echo "" >> "$temp_file"
        elif [[ "$line" =~ ^\[\[SECTION\]\]$ ]]; then
            # Add blank line after [[SECTION]]
            echo "" >> "$temp_file"
        elif [[ "$line" =~ ^\[\[/SECTION\]\]$ ]]; then
            # Add blank line after [[/SECTION]]
            echo "" >> "$temp_file"
        elif [[ "$line" =~ ^\[REQUIREMENT\]$ ]]; then
            # Add blank line after [REQUIREMENT]
            echo "" >> "$temp_file"
        elif [[ "$line" =~ ^\[\[/REQUIREMENT\]\]$ ]]; then
            # Add blank line after [[/REQUIREMENT]]
            echo "" >> "$temp_file"
        fi
    done < "$file"
    
    # Check if the file was actually changed
    if ! cmp -s "$file" "$temp_file"; then
        echo "NORMALIZED"
        mv "$temp_file" "$file"
        NORMALIZED_COUNT=$((NORMALIZED_COUNT + 1))
    else
        echo "OK"
        rm "$temp_file"
        ALREADY_CORRECT=$((ALREADY_CORRECT + 1))
    fi
done

echo
echo "=== Normalization Results ==="
echo "Total files processed: $TOTAL_FILES"
echo "Files normalized: $NORMALIZED_COUNT"
echo "Files already correct: $ALREADY_CORRECT"

if [ $NORMALIZED_COUNT -gt 0 ]; then
    echo
    echo "✓ Normalized $NORMALIZED_COUNT files for StrictDoc compatibility!"
    echo "Run validation script to verify all files now work."
else
    echo
    echo "✓ All files already have correct formatting!"
fi 