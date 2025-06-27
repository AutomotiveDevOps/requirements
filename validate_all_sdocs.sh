#!/bin/bash

# Validate all .sdoc files in the project
# This script attempts to parse each .sdoc file with StrictDoc to check for syntax errors

set -e

echo "=== StrictDoc File Validation ==="
echo "Validating all .sdoc files in the project..."
echo

# Find all .sdoc files
SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

TOTAL_FILES=0
SUCCESS_COUNT=0
FAILED_FILES=()

# Process each file
for file in $SDOC_FILES; do
    TOTAL_FILES=$((TOTAL_FILES + 1))
    echo -n "[$TOTAL_FILES] Testing: $file ... "
    
    # Try to parse the file with StrictDoc
    if venv/bin/strictdoc export "$file" --formats html --output-dir "/tmp/strictdoc_validation_$$" >/dev/null 2>&1; then
        echo "✓ PASS"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        echo "✗ FAIL"
        FAILED_FILES+=("$file")
    fi
done

echo
echo "=== Validation Results ==="
echo "Total files tested: $TOTAL_FILES"
echo "Successful: $SUCCESS_COUNT"
echo "Failed: $((TOTAL_FILES - SUCCESS_COUNT))"

if [ ${#FAILED_FILES[@]} -gt 0 ]; then
    echo
    echo "=== Failed Files ==="
    for file in "${FAILED_FILES[@]}"; do
        echo "  - $file"
    done
    echo
    echo "=== Detailed Error Analysis ==="
    for file in "${FAILED_FILES[@]}"; do
        echo "File: $file"
        echo "Error:"
        venv/bin/strictdoc export "$file" --formats html --output-dir "/tmp/strictdoc_validation_$$" 2>&1 | head -5
        echo "---"
    done
    exit 1
else
    echo
    echo "✓ All .sdoc files are valid!"
    exit 0
fi 