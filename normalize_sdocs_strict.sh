#!/bin/bash

# Strict normalization of .sdoc files for StrictDoc grammar
# - No blank lines between fields in [REQUIREMENT] blocks
# - Correct field order: UID, STATUS (optional), TAGS (optional), TITLE, STATEMENT, RATIONALE
# - Exactly one blank line after document TITLE
# - Remove trailing spaces

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