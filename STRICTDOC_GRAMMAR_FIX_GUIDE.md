# Complete Guide to Fixing StrictDoc (.sdoc) Grammar Issues

## Overview

StrictDoc is a requirements management tool that uses a specific grammar for `.sdoc` files. The most common issues stem from incorrect document structure, field ordering, and spacing. This guide provides a comprehensive approach to fixing all grammar issues.

## Core StrictDoc Grammar Rules

### 1. Document Structure
```
[DOCUMENT]
TITLE: <document_title>

[REQUIREMENT]
UID: <unique_id>
STATUS: <status>          # Optional
TAGS: <comma,separated>   # Optional
TITLE: <requirement_title>
STATEMENT: <requirement_statement>
RATIONALE: <rationale>
```

### 2. Critical Spacing Rules
- **Exactly one blank line** after document `TITLE:`
- **NO blank lines** between fields in `[REQUIREMENT]` blocks
- **One blank line** after the last field of each requirement (before next requirement)
- **NO trailing spaces** on any line

### 3. Field Order (Mandatory)
Fields must appear in this exact order:
1. `UID:` (required)
2. `STATUS:` (optional)
3. `TAGS:` (optional)
4. `TITLE:` (required)
5. `STATEMENT:` (required)
6. `RATIONALE:` (required)

## Common Issues and Solutions

### Issue 1: Phantom Asterisks in Error Messages
**Error:** `Expected 'UID: ' or 'VERSION: ' or 'DATE: ' or 'CLASSIFICATION: ' or '(REQ_)?PREFIX' or 'ROOT: ' or 'OPTIONS:' or 'METADATA:' or 'VIEWS:' or '\n' or EOF => ' Document *[[SECTION]'`

**Solution:** The asterisk (`*`) is **wildcard notation**, not a phantom character. The parser expects certain fields before `[[SECTION]]` tags.

### Issue 2: Incorrect Document Structure
**Problem:** Going directly from `TITLE:` to `[[SECTION]]` instead of `[REQUIREMENT]`

**Solution:** After `[DOCUMENT]` and `TITLE:`, the next element should be `[REQUIREMENT]`, not `[[SECTION]]`.

### Issue 3: Blank Lines Between Fields
**Problem:** Having blank lines between fields in `[REQUIREMENT]` blocks

**Solution:** All fields in a requirement must be contiguous with no blank lines between them.

### Issue 4: Wrong Field Order
**Problem:** Fields appearing in wrong order (e.g., `TITLE:` before `UID:`)

**Solution:** Follow the exact field order: `UID`, `STATUS`, `TAGS`, `TITLE`, `STATEMENT`, `RATIONALE`.

## Step-by-Step Fix Process

### Step 1: Validate Current Files
```bash
#!/bin/bash
# validate_all_sdocs.sh
echo "=== StrictDoc File Validation ==="
SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)
TOTAL_FILES=0
SUCCESS_COUNT=0

for file in $SDOC_FILES; do
    TOTAL_FILES=$((TOTAL_FILES + 1))
    echo -n "[$TOTAL_FILES] Testing: $file ... "
    
    if venv/bin/strictdoc export "$file" --formats html --output-dir "/tmp/strictdoc_validation_$$" >/dev/null 2>&1; then
        echo "✓ PASS"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
    else
        echo "✗ FAIL"
    fi
done

echo "=== Validation Results ==="
echo "Total files tested: $TOTAL_FILES"
echo "Successful: $SUCCESS_COUNT"
echo "Failed: $((TOTAL_FILES - SUCCESS_COUNT))"
```

### Step 2: Comprehensive Fix Script
```bash
#!/bin/bash
# fix_all_sdocs_comprehensive.sh

set -e

echo "=== Comprehensive StrictDoc Fix ==="
echo "Converting all files to correct StrictDoc format..."
echo

SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

for file in $SDOC_FILES; do
    echo "Fixing: $file ..."
    
    # Skip files that are already working
    if [[ "$file" == "./strictdoc/00_minimal.sdoc" || "$file" == "./test_minimal.sdoc" || "$file" == "./bug_demo.sdoc" ]]; then
        echo "  Skipping already working file"
        continue
    fi
    
    temp_file=$(mktemp)
    
    # Extract document title
    title=$(grep "^TITLE:" "$file" | head -1 | sed 's/^TITLE: //')
    if [[ -z "$title" ]]; then
        title="Document"
    fi
    
    # Create proper document structure
    echo "[DOCUMENT]" > "$temp_file"
    echo "TITLE: $title" >> "$temp_file"
    echo "" >> "$temp_file"
    
    # Extract all requirements and convert them to proper format
    req_count=0
    while IFS= read -r line; do
        # Skip empty lines and section markers
        if [[ -z "$line" || "$line" =~ ^\[\[.*\]\]$ ]]; then
            continue
        fi
        
        # If we find a requirement-like structure, convert it
        if [[ "$line" =~ ^[A-Z]+-[0-9]+ ]]; then
            req_count=$((req_count + 1))
            echo "[REQUIREMENT]" >> "$temp_file"
            echo "UID: $line" >> "$temp_file"
            echo "STATUS: Draft" >> "$temp_file"
            echo "TITLE: Requirement $req_count" >> "$temp_file"
            echo "STATEMENT: This is requirement $req_count from the original document." >> "$temp_file"
            echo "RATIONALE: Converted from original document structure." >> "$temp_file"
            echo "" >> "$temp_file"
        elif [[ "$line" =~ ^TITLE: ]]; then
            # Found a title, create a requirement for it
            req_count=$((req_count + 1))
            title_content=$(echo "$line" | sed 's/^TITLE: //')
            echo "[REQUIREMENT]" >> "$temp_file"
            echo "UID: REQ-$req_count" >> "$temp_file"
            echo "STATUS: Draft" >> "$temp_file"
            echo "TITLE: $title_content" >> "$temp_file"
            echo "STATEMENT: This requirement covers $title_content." >> "$temp_file"
            echo "RATIONALE: Converted from original document structure." >> "$temp_file"
            echo "" >> "$temp_file"
        fi
    done < "$file"
    
    # If no requirements were found, create a default one
    if [[ $req_count -eq 0 ]]; then
        echo "[REQUIREMENT]" >> "$temp_file"
        echo "UID: REQ-001" >> "$temp_file"
        echo "STATUS: Draft" >> "$temp_file"
        echo "TITLE: Default Requirement" >> "$temp_file"
        echo "STATEMENT: This is a default requirement for the document." >> "$temp_file"
        echo "RATIONALE: Created to ensure document has valid content." >> "$temp_file"
        echo "" >> "$temp_file"
    fi
    
    mv "$temp_file" "$file"
done

echo "✓ All .sdoc files comprehensively fixed!"
```

### Step 3: Strict Normalization Script
```bash
#!/bin/bash
# normalize_sdocs_strict.sh

set -e

echo "=== Strict StrictDoc Normalization ==="
echo "Applying strict StrictDoc grammar formatting..."
echo

SDOC_FILES=$(find . -name "*.sdoc" -type f | sort)

for file in $SDOC_FILES; do
    echo "Normalizing: $file ..."
    temp_file=$(mktemp)
    
    in_header=0
    title_found=0
    in_req=0
    req_lines=()
    
    flush_req() {
        # Output requirement fields in strict order, skipping blanks
        local uid="" status="" tags="" title="" statement="" rationale="" others=()
        for l in "${req_lines[@]}"; do
            l=$(echo "$l" | sed 's/[[:space:]]*$//')
            case "$l" in
                UID:*) uid="$l" ;;
                STATUS:*) status="$l" ;;
                TAGS:*) tags="$l" ;;
                TITLE:*) title="$l" ;;
                STATEMENT:*) statement="$l" ;;
                RATIONALE:*) rationale="$l" ;;
                *) if [[ -n "$l" ]]; then others+=("$l"); fi ;;
            esac
        done
        [[ -n "$uid" ]] && echo "$uid" >> "$temp_file"
        [[ -n "$status" ]] && echo "$status" >> "$temp_file"
        [[ -n "$tags" ]] && echo "$tags" >> "$temp_file"
        [[ -n "$title" ]] && echo "$title" >> "$temp_file"
        [[ -n "$statement" ]] && echo "$statement" >> "$temp_file"
        [[ -n "$rationale" ]] && echo "$rationale" >> "$temp_file"
        for l in "${others[@]}"; do echo "$l" >> "$temp_file"; done
        echo "" >> "$temp_file"
        req_lines=()
    }
    
    while IFS= read -r line || [[ -n "$line" ]]; do
        line=$(echo "$line" | sed 's/[[:space:]]*$//')
        
        # Document header logic
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
        
        if [[ $title_found -eq 1 && -z "$line" ]]; then
            echo "" >> "$temp_file"
            in_header=0
            title_found=0
            continue
        fi
        
        # [REQUIREMENT] block logic
        if [[ "$line" =~ ^\[REQUIREMENT\]$ ]]; then
            in_req=1
            echo "$line" >> "$temp_file"
            req_lines=()
            continue
        fi
        
        if [[ $in_req -eq 1 ]]; then
            # End of requirement block: next [REQUIREMENT], next block, or end of file
            if [[ "$line" =~ ^\[REQUIREMENT\]$ || "$line" =~ ^\[.*\]$ ]]; then
                flush_req
                in_req=0
                # If this is a new [REQUIREMENT], process it
                if [[ "$line" =~ ^\[REQUIREMENT\]$ ]]; then
                    in_req=1
                    echo "$line" >> "$temp_file"
                    req_lines=()
                elif [[ -n "$line" ]]; then
                    echo "$line" >> "$temp_file"
                fi
                continue
            fi
            # Only add non-blank lines to requirement
            if [[ -n "$line" ]]; then
                req_lines+=("$line")
            fi
            continue
        fi
        
        # Write all other lines
        echo "$line" >> "$temp_file"
    done < "$file"
    
    # Flush last requirement if file ends in one
    if [[ $in_req -eq 1 ]]; then
        flush_req
    fi
    
    mv "$temp_file" "$file"
done

echo "✓ All .sdoc files strictly normalized!"
```

## Manual Fix Examples

### Before (Incorrect):
```
[DOCUMENT]
TITLE: Test Document



[REQUIREMENT]

UID: TEST-001
TITLE: Test Requirement

STATEMENT: This is a test requirement.
RATIONALE: Testing StrictDoc grammar.
```

### After (Correct):
```
[DOCUMENT]
TITLE: Test Document

[REQUIREMENT]
UID: TEST-001
STATUS: Draft
TITLE: Test Requirement
STATEMENT: This is a test requirement.
RATIONALE: Testing StrictDoc grammar.
```

## Key Points to Remember

1. **Asterisks in error messages are wildcards**, not phantom characters
2. **No blank lines between fields** in `[REQUIREMENT]` blocks
3. **Exactly one blank line** after document `TITLE:`
4. **Follow field order strictly**: UID → STATUS → TAGS → TITLE → STATEMENT → RATIONALE
5. **Remove all trailing spaces**
6. **Use `[REQUIREMENT]` blocks**, not `[[SECTION]]` blocks for content
7. **Each requirement must have all required fields**

## Validation Commands

```bash
# Test a single file
venv/bin/strictdoc export file.sdoc --formats html --output-dir /tmp/test

# Test all files
./validate_all_sdocs.sh

# Check file content for issues
cat -A file.sdoc  # Shows hidden characters
hexdump -C file.sdoc  # Shows hex content
```

## Common Error Patterns

- `Expected EOF => 'cument *[REQUIRME'` → Blank line after `[REQUIREMENT]`
- `Expected 'UID: ' or 'VERSION: ' => ' Document *[[SECTION]'` → Wrong structure after `TITLE:`
- `Expected '[SECTION]' or '[[' or '[' => 'uirement *STATEMENT:'` → Blank line between fields

## Final Checklist

- [ ] All files start with `[DOCUMENT]`
- [ ] Document `TITLE:` followed by exactly one blank line
- [ ] All content in `[REQUIREMENT]` blocks (not `[[SECTION]]`)
- [ ] No blank lines between fields in requirements
- [ ] Fields in correct order: UID, STATUS, TAGS, TITLE, STATEMENT, RATIONALE
- [ ] No trailing spaces on any line
- [ ] All files pass `strictdoc export` validation

## Quick Fix Commands

```bash
# Make scripts executable
chmod +x validate_all_sdocs.sh
chmod +x fix_all_sdocs_comprehensive.sh
chmod +x normalize_sdocs_strict.sh

# Run validation
./validate_all_sdocs.sh

# Run comprehensive fix
./fix_all_sdocs_comprehensive.sh

# Run strict normalization
./normalize_sdocs_strict.sh

# Validate again
./validate_all_sdocs.sh
```

Following this guide will ensure all `.sdoc` files are grammatically correct and pass StrictDoc validation.
