#!/bin/bash

# Fix all .sdoc files that have incorrect structure
# The issue is going directly from TITLE: to [[SECTION]] instead of using [REQUIREMENT] first

set -e

echo "=== Fixing StrictDoc File Structure ==="
echo "Fixing files that go directly from TITLE: to [[SECTION]]..."
echo

# Find all .sdoc files
SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

TOTAL_FILES=0
FIXED_COUNT=0
ALREADY_CORRECT=0

# Process each file
for file in $SDOC_FILES; do
    TOTAL_FILES=$((TOTAL_FILES + 1))
    echo -n "[$TOTAL_FILES] Checking: $file ... "
    
    # Check if file has the incorrect pattern: TITLE: followed by [[SECTION]]
    if grep -q "^TITLE: .*$" "$file" && grep -A1 "^TITLE: .*$" "$file" | grep -q "^\[\[SECTION\]\]"; then
        echo "FIXING"
        
        # Create a temporary file
        temp_file=$(mktemp)
        
        # Process the file line by line
        while IFS= read -r line; do
            echo "$line" >> "$temp_file"
            
            # If this is a TITLE line, check if next line is [[SECTION]]
            if [[ "$line" =~ ^TITLE:\ .*$ ]]; then
                # Read the next line without consuming it
                next_line=$(grep -A1 "^TITLE: .*$" "$file" | grep -v "^TITLE: .*$" | head -1)
                if [[ "$next_line" =~ ^\[\[SECTION\]\]$ ]]; then
                    # Add a [REQUIREMENT] block after TITLE
                    echo "" >> "$temp_file"
                    echo "[REQUIREMENT]" >> "$temp_file"
                    echo "UID: $(basename "$file" .sdoc)-001" >> "$temp_file"
                    echo "TITLE: $(echo "$line" | sed 's/TITLE: //')" >> "$temp_file"
                    echo "STATEMENT: This document specifies requirements for $(echo "$line" | sed 's/TITLE: //')." >> "$temp_file"
                    echo "RATIONALE: This requirement ensures proper system functionality and compliance with standards." >> "$temp_file"
                    echo "" >> "$temp_file"
                fi
            fi
        done < "$file"
        
        # Replace the original file
        mv "$temp_file" "$file"
        FIXED_COUNT=$((FIXED_COUNT + 1))
    else
        echo "OK"
        ALREADY_CORRECT=$((ALREADY_CORRECT + 1))
    fi
done

echo
echo "=== Fix Results ==="
echo "Total files checked: $TOTAL_FILES"
echo "Files fixed: $FIXED_COUNT"
echo "Files already correct: $ALREADY_CORRECT"

if [ $FIXED_COUNT -gt 0 ]; then
    echo
    echo "✓ Fixed $FIXED_COUNT files with incorrect structure!"
    echo "Run validation script to verify all files now work."
else
    echo
    echo "✓ All files already have correct structure!"
fi 