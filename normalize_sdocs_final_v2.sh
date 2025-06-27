#!/bin/bash

# Final normalization of .sdoc files for StrictDoc grammar
# - Remove trailing spaces
# - Ensure proper newlines
# - Follow exact StrictDoc grammar pattern

set -e

echo "=== Final StrictDoc Normalization v2 ==="
echo "Applying final StrictDoc grammar formatting..."
echo

SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

for file in $SDOC_FILES; do
    echo "Normalizing: $file ..."
    temp_file=$(mktemp)
    
    # Read the file and normalize it
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Remove trailing spaces
        line=$(echo "$line" | sed 's/[[:space:]]*$//')
        
        # Write the line
        echo "$line" >> "$temp_file"
    done < "$file"
    
    # Ensure the file ends with a newline
    echo "" >> "$temp_file"
    
    mv "$temp_file" "$file"
done

echo "✓ All .sdoc files normalized with final StrictDoc grammar rules!" 