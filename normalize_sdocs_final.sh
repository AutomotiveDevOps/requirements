#!/bin/bash

# Final normalization of .sdoc files for StrictDoc grammar
# - No blank line after block headers ([REQUIREMENT], [[SECTION]], etc.)
# - Exactly one blank line after TITLE: in document header
# - Blank lines only between major blocks, never after block headers

set -e

echo "=== Final StrictDoc Normalization ==="
echo "Applying final StrictDoc grammar formatting..."
echo

SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

for file in $SDOC_FILES; do
    echo "Normalizing: $file ..."
    temp_file=$(mktemp)
    
    in_header=0
    skip_next_empty=0
    
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Handle document header
        if [[ "$line" =~ ^\[DOCUMENT\]$ ]]; then
            in_header=1
            echo "$line" >> "$temp_file"
            continue
        fi
        
        if [[ $in_header -eq 1 && "$line" =~ ^TITLE: ]]; then
            echo "$line" >> "$temp_file"
            echo "" >> "$temp_file"  # One blank line after TITLE in header
            in_header=0
            continue
        fi
        
        # Handle block headers - no blank line after them
        if [[ "$line" =~ ^\[REQUIREMENT\]$ || "$line" =~ ^\[\[SECTION\]\]$ || "$line" =~ ^\[\[/SECTION\]\]$ || "$line" =~ ^\[\[/REQUIREMENT\]\]$ ]]; then
            echo "$line" >> "$temp_file"
            skip_next_empty=1  # Skip next empty line
            continue
        fi
        
        # Skip empty line if it follows a block header
        if [[ $skip_next_empty -eq 1 && -z "$line" ]]; then
            skip_next_empty=0
            continue
        fi
        
        # Write the line
        echo "$line" >> "$temp_file"
        skip_next_empty=0
    done < "$file"
    
    mv "$temp_file" "$file"
done

echo "✓ All .sdoc files normalized with final StrictDoc grammar rules!" 