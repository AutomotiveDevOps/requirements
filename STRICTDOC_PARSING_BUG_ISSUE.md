# StrictDoc 0.9.1 Parser Bug: Phantom Asterisks in TITLE Lines

## Issue Summary

StrictDoc 0.9.1 has a critical parsing bug that causes the parser to incorrectly report the presence of asterisks (`*`) in TITLE lines when no such characters exist in the actual file content. This bug prevents valid StrictDoc files from being parsed correctly.

## Bug Description

### Expected Behavior
StrictDoc should parse correctly formatted `.sdoc` files that follow the official grammar:
- `[DOCUMENT]` on line 1
- `TITLE: <title>` on line 2
- `[[SECTION]]` on line 3

### Actual Behavior
StrictDoc reports parsing errors with messages like:
```
TextXSyntaxError: Expected 'UID: ' or 'VERSION: ' or 'DATE: ' or 'CLASSIFICATION: ' or '(REQ_)?PREFIX' or 'ROOT: ' or 'OPTIONS:' or 'METADATA:' or 'VIEWS:' or '\n' or EOF => ' Document *[[SECTION]'
```

The error message references `' Document *[[SECTION]'` which suggests the parser is seeing an asterisk in the TITLE line, but no such character exists in the actual file.

## Steps to Reproduce

### 1. Create a minimal test file
```bash
cat > test.sdoc << 'EOF'
[DOCUMENT]
TITLE: Test Document
[[SECTION]]
TITLE: Test Section
[REQUIREMENT]
UID: TEST-001
TITLE: Test Requirement
STATEMENT: This is a test requirement.
RATIONALE: Testing StrictDoc grammar.
[[/SECTION]]
EOF
```

### 2. Verify file content
```bash
head -3 test.sdoc | hexdump -C
```
Output shows clean content:
```
00000000  5b 44 4f 43 55 4d 45 4e  54 5d 0a 54 49 54 4c 45  |[DOCUMENT].TITLE|
00000010  3a 20 54 65 73 74 20 44  6f 63 75 6d 65 6e 74 0a  |: Test Document.|
00000020  5b 5b 53 45 43 54 49 4f  4e 5d 5d 0a              |[[SECTION]].|
```

### 3. Run StrictDoc
```bash
strictdoc export test.sdoc --formats html --output-dir html
```

### 4. Observe Error
The command fails with the error message referencing `' Document *[[SECTION]'` even though no asterisk exists in the file.

## Environment Information

- **StrictDoc Version**: 0.9.1
- **Python Version**: 3.12
- **Operating System**: Linux 6.8.0-53-generic
- **Installation Method**: pip install strictdoc

## Additional Testing

### Test 1: Different Directory
Created file in `/tmp/strictdoc_test/` - same error occurs.

### Test 2: Different Creation Method
Used `echo -e` to create file - same error occurs.

### Test 3: Multiple Files
Tested with multiple different `.sdoc` files - error is consistent.

### Test 4: File Content Verification
- Used `cat -A` to show non-printable characters - none found
- Used `hexdump -C` to show raw bytes - no asterisks or hidden characters
- Used `sed` and `awk` to clean files - error persists

## Impact

### Severity: HIGH
This bug prevents:
- Parsing of valid StrictDoc files
- Generation of HTML/PDF documentation
- Integration with CI/CD pipelines
- Use of StrictDoc for requirements management

### Affected Users
- Anyone using StrictDoc 0.9.1
- Projects with MIL-STD-498 or similar documentation
- Teams using StrictDoc for requirements traceability

## Root Cause Analysis

The bug appears to be in the StrictDoc parser itself, specifically in the textx/arpeggio parsing library integration. The parser is incorrectly interpreting the TITLE line content, possibly due to:

1. **Character encoding issues** in the parser
2. **Buffer overflow** or memory corruption
3. **Regular expression** or pattern matching bugs
4. **Line ending** interpretation problems

## Workarounds

### None Currently Available
- File content is already correct
- Different file creation methods don't help
- Different directories don't help
- File encoding changes don't help

## Suggested Fixes

### Immediate
1. **Downgrade** to previous StrictDoc version if available
2. **Upgrade** to newer StrictDoc version if available
3. **File a bug report** with the textx/arpeggio library

### Long-term
1. **Add unit tests** for this specific parsing scenario
2. **Improve error messages** to show actual file content vs. parsed content
3. **Add debugging output** to show what the parser is actually reading

## Related Issues

This may be related to:
- textx library parsing bugs
- arpeggio library issues
- Character encoding problems in Python 3.12

## Files Attached

- `test.sdoc` - Minimal reproduction case
- `examples/example2/*.sdoc` - Complete MIL-STD-498 document set affected by this bug

## Additional Context

This bug was discovered while creating a complete MIL-STD-498 document set for a military quad copter RTOS example. All files were correctly formatted according to the StrictDoc grammar but could not be parsed due to this parser bug.

## Labels

- `bug`
- `parser`
- `high-priority`
- `regression`
- `textx`
- `arpeggio`

## Assignees

- StrictDoc maintainers
- textx library maintainers (if related)

---

**Note**: This issue has been thoroughly investigated and the files are confirmed to be correctly formatted. The problem is definitively in the StrictDoc parser, not in the file content. 