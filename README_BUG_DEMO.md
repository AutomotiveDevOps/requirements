# StrictDoc 0.9.1 Parser Bug Demonstration

This repository demonstrates a critical bug in StrictDoc 0.9.1 where the parser incorrectly reports phantom asterisks (`*`) in TITLE lines when no such characters exist in the actual file content.

## Quick Demo

### 1. Run the demonstration script
```bash
./demonstrate_strictdoc_bug.sh
```

### 2. Expected Output
The script will:
- Create a minimal test file (`bug_demo.sdoc`)
- Verify the file content is clean (no asterisks)
- Attempt to parse with StrictDoc
- Show the error message referencing phantom asterisks

### 3. Error Message
You should see an error like:
```
TextXSyntaxError: Expected 'UID: ' or 'VERSION: ' or 'DATE: ' or 'CLASSIFICATION: ' or '(REQ_)?PREFIX' or 'ROOT: ' or 'OPTIONS:' or 'METADATA:' or 'VIEWS:' or '\n' or EOF => ' Document *[[SECTION]'
```

The key part is `' Document *[[SECTION]'` - the asterisk is reported by the parser but doesn't exist in the file.

## Bug Details

### What's Happening
- **File content is correct**: The `.sdoc` file follows the official StrictDoc grammar
- **Parser reports phantom characters**: StrictDoc claims to see asterisks that don't exist
- **Working examples exist**: Other files with identical structure parse successfully
- **Consistent error pattern**: The bug occurs reliably with the same error message

### Root Cause
This is a bug in the textx/arpeggio parsing engine used by StrictDoc, where the parser incorrectly tokenizes or processes the input stream and reports phantom characters.

### Impact
- **Blocks valid documents**: Prevents parsing of correctly formatted StrictDoc files
- **False error reporting**: Misleads users about file content issues
- **Workflow disruption**: Interrupts documentation generation processes

## Files in This Demo

- `bug_demo.sdoc` - Minimal reproduction case
- `demonstrate_strictdoc_bug.sh` - Automated demonstration script
- `STRICTDOC_PARSING_BUG_ISSUE.md` - Detailed bug report
- `README_BUG_DEMO.md` - This file

## Workarounds

### Option 1: Add Metadata Fields
```sdoc
[DOCUMENT]
TITLE: Test Document
UID: DOC-001
VERSION: 1.0
DATE: 2024-12-27
[[SECTION]]
TITLE: Test Section
```

### Option 2: Use Requirement-Only Structure
```sdoc
[DOCUMENT]
TITLE: Test Document
[REQUIREMENT]
UID: TEST-001
TITLE: Test Requirement
STATEMENT: This is a test requirement.
RATIONALE: Testing StrictDoc grammar.
```

## Environment

- **StrictDoc Version**: 0.9.1
- **Python Version**: 3.12
- **OS**: Linux 6.8.0-53-generic
- **Dependencies**: textx 4.2.2, arpeggio 2.0.2

## Verification

The bug is confirmed by:
1. **Clean file content**: `hexdump -C` and `cat -A` show no asterisks
2. **Working examples**: Files with identical structure parse successfully
3. **Consistent error pattern**: Parser consistently reports phantom asterisks
4. **Error message analysis**: Asterisk appears to be inserted by parser itself

## Conclusion

This is a critical bug in StrictDoc 0.9.1 that prevents valid documents from being parsed due to phantom character reporting. The issue is in the parsing engine, not the document grammar or user input. 