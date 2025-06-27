# StrictDoc 0.9.1 Parser Bug Demonstration

This repository contains a simple demonstration of the StrictDoc 0.9.1 parsing bug that causes phantom asterisk errors.

## Quick Demo

### 1. Install StrictDoc
```bash
pip install strictdoc
```

### 2. Create a test file
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

### 3. Verify the file is clean
```bash
head -3 test.sdoc | hexdump -C
```

### 4. Run StrictDoc (this will fail)
```bash
strictdoc export test.sdoc --formats html --output-dir html
```

### 5. Observe the error
The error message will show:
```
TextXSyntaxError: Expected 'UID: ' or 'VERSION: ' or 'DATE: ' or 'CLASSIFICATION: ' or '(REQ_)?PREFIX' or 'ROOT: ' or 'OPTIONS:' or 'METADATA:' or 'VIEWS:' or '\n' or EOF => ' Document *[[SECTION]'
```

**The key issue**: The error references `' Document *[[SECTION]'` but no asterisk exists in the file!

## Files in this Repository

- `bug_demo.sdoc` - Simple test file that triggers the bug
- `demonstrate_strictdoc_bug.sh` - Automated demonstration script
- `STRICTDOC_PARSING_BUG_ISSUE.md` - Complete GitHub issue report

## Run the Automated Demo

```bash
chmod +x demonstrate_strictdoc_bug.sh
./demonstrate_strictdoc_bug.sh
```

## What This Proves

1. **File is correctly formatted** - Follows StrictDoc grammar exactly
2. **No hidden characters** - Hexdump shows clean content
3. **No asterisks exist** - Character count confirms this
4. **StrictDoc reports phantom asterisk** - Parser bug confirmed

## Environment

- StrictDoc Version: 0.9.1
- Python Version: 3.12
- Operating System: Linux

## Impact

This bug prevents:
- Parsing of valid StrictDoc files
- Generation of HTML/PDF documentation
- Integration with CI/CD pipelines
- Use of StrictDoc for requirements management

## Next Steps

1. Report this issue to the StrictDoc project
2. Consider downgrading to a previous version
3. Wait for a fix in a future release 