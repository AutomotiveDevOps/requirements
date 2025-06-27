# ADAS Control Module - MIL-STD-498 Documentation Example

This directory contains a comprehensive example of MIL-STD-498 documentation for a fictitious Advanced Driver Assistance System (ADAS) Control Module. The example demonstrates a complete 1:1 mapping to the MIL-STD-498 standard document structure.

## Overview

The ADAS Control Module is a safety-critical automotive system that provides driver assistance capabilities including:
- Adaptive Cruise Control
- Lane Keeping Assistance  
- Collision Avoidance
- Automated Emergency Braking
- Blind Spot Monitoring
- Pedestrian Detection

## Quick Start - Viewing the Documentation

### Option 1: View Online (Recommended)
The HTML documentation is included in this repository and can be viewed directly:

1. **Main Index**: Open `docs/html/index.html` in any web browser
2. **Individual Documents**: Navigate to `docs/html/example1/` for specific document views
3. **Multiple Formats**: Each document has 4 viewing formats:
   - **Standard View**: `DOCUMENT.html` (e.g., `SRS.html`)
   - **Table View**: `DOCUMENT-TABLE.html` (e.g., `SRS-TABLE.html`)
   - **Traceability View**: `DOCUMENT-TRACE.html` (e.g., `SRS-TRACE.html`)
   - **Deep Traceability View**: `DOCUMENT-DEEP-TRACE.html` (e.g., `SRS-DEEP-TRACE.html`)

### Option 2: Local Web Server
For the best experience, serve the files using a local web server:

```bash
# Using Python 3
cd docs/html
python3 -m http.server 8000

# Using Python 2
cd docs/html
python -m SimpleHTTPServer 8000

# Using Node.js (if installed)
cd docs/html
npx serve .

# Then open http://localhost:8000 in your browser
```

### Option 3: GitHub Pages
If this repository is hosted on GitHub, the HTML files can be viewed directly through GitHub Pages or by browsing the repository contents.

## Building the Documentation

### Prerequisites
- Python 3.8 or higher
- Virtual environment with StrictDoc installed

### Step-by-Step Build Instructions

1. **Navigate to the project directory**:
   ```bash
   cd /projects/requirements/examples/example1
   ```

2. **Activate the virtual environment**:
   ```bash
   source /projects/requirements/venv/bin/activate
   ```

3. **Build all documents**:
   ```bash
   strictdoc export . --output-dir docs --formats html
   ```

4. **Build individual documents** (optional):
   ```bash
   # Build just the SRS
   strictdoc export SRS.sdoc --output-dir docs --formats html
   
   # Build multiple specific documents
   strictdoc export SRS.sdoc SDD.sdoc STP.sdoc --output-dir docs --formats html
   ```

5. **View the results**:
   ```bash
   # Open the main index
   xdg-open docs/html/index.html  # Linux
   open docs/html/index.html      # macOS
   start docs/html/index.html     # Windows
   ```

### Build Options

The `strictdoc export` command supports various options:

```bash
# Build with specific output formats
strictdoc export . --output-dir docs --formats html,rst

# Build with parallel processing (faster)
strictdoc export . --output-dir docs --formats html --parallel

# Build with custom configuration
strictdoc export . --output-dir docs --formats html --config-file strictdoc.toml

# Build with verbose output
strictdoc export . --output-dir docs --formats html --verbose
```

### Output Structure

After building, the following structure is created:

```
docs/
├── html/
│   ├── index.html              # Main navigation page
│   ├── _static/                # CSS, JS, and assets
│   └── example1/               # Generated document files
│       ├── SRS.html            # Software Requirements Specification
│       ├── SRS-TABLE.html      # Requirements table view
│       ├── SRS-TRACE.html      # Traceability matrix
│       ├── SRS-DEEP-TRACE.html # Detailed traceability
│       ├── SDD.html            # Software Design Description
│       └── ...                 # All other documents
```

## MIL-STD-498 Document Set

This example includes all 20 MIL-STD-498 document types with complete section and requirement mappings:

### Core Requirements Documents
- **SRS.sdoc** - Software Requirements Specification
- **SDD.sdoc** - Software Design Description
- **STP.sdoc** - Software Test Plan
- **STD.sdoc** - Software Test Description
- **STR.sdoc** - Software Test Report
- **STRP.sdoc** - Software Test Report (Phase)

### System-Level Documents
- **OCD.sdoc** - Operational Concept Document
- **SSS.sdoc** - Software System Specification
- **SSDD.sdoc** - Software System Design Description

### Interface Documents
- **IRS.sdoc** - Interface Requirements Specification
- **IDD.sdoc** - Interface Design Document

### Product and Version Documents
- **SPS.sdoc** - Software Product Specification
- **SVD.sdoc** - Software Version Description

### Database and Data Documents
- **DBDD.sdoc** - Database Design Description

### User and Support Documents
- **SUM.sdoc** - Software User Manual
- **SDP.sdoc** - Software Development Plan
- **CPM.sdoc** - Computer Program Manual
- **FSM.sdoc** - Firmware Support Manual

### Additional Documents
- **COM.sdoc** - Common Elements (if needed)

## Document Structure

Each document follows the exact MIL-STD-498 section structure with:
- Proper document identification
- Scope and overview sections
- Referenced documents
- Detailed requirements/design sections
- Notes and traceability

## Requirements Coverage

The example demonstrates comprehensive requirements coverage across:
- **35 SRS Requirements** - Complete software requirements specification
- **22 SDD Requirements** - Detailed design requirements
- **18 STP Requirements** - Comprehensive test planning
- **15 STD Requirements** - Detailed test procedures
- **15 STR Requirements** - Test results and analysis
- **15 STRP Requirements** - Phase-specific test reporting
- **26 OCD Requirements** - Operational concept and scenarios
- **21 SSS Requirements** - System-level specifications
- **14 SSDD Requirements** - System design architecture
- **16 IRS Requirements** - Interface requirements
- **14 IDD Requirements** - Interface design details
- **16 SPS Requirements** - Product specifications
- **11 SVD Requirements** - Version and delivery specifications
- **12 DBDD Requirements** - Database design and management
- **10 CPM Requirements** - Program manual and procedures
- **9 FSM Requirements** - Firmware support procedures

## Automotive Context

All documents are tailored for automotive safety-critical applications with:
- ISO 26262 ASIL D compliance requirements
- MISRA C++ coding standards
- AUTOSAR architecture considerations
- Automotive communication protocols (CAN, FlexRay, Ethernet)
- Real-time performance requirements
- Environmental and safety constraints

## Document Relationships

The documents maintain proper traceability relationships:
- SRS → SDD → Implementation
- SRS → STP → STD → STR/STRP
- OCD → SRS → SSS → SSDD
- IRS → IDD → Implementation
- SRS → SPS → SVD
- All documents → Configuration Management

## Quality Assurance

Each document includes:
- Unique requirement identifiers (UID)
- Clear requirement statements
- Rationale for each requirement
- Proper section hierarchy
- Traceability to related documents

## Compliance

This example demonstrates compliance with:
- MIL-STD-498 document structure requirements
- Automotive safety standards (ISO 26262)
- Software development best practices
- Requirements engineering principles
- Configuration management practices

## Troubleshooting

### Common Issues

1. **Build fails with parsing errors**:
   - Ensure all SDoc files have proper syntax
   - Check for malformed SECTION tags
   - Verify no trailing characters after closing tags

2. **HTML files not generated**:
   - Verify StrictDoc is installed in the virtual environment
   - Check that SDoc files exist in the current directory
   - Ensure write permissions for the output directory

3. **Missing styles or broken links**:
   - Use a local web server instead of opening files directly
   - Check that `_static` directory is present in the output

### Performance Tips

- Use `--parallel` flag for faster builds with multiple documents
- Build individual documents during development for faster iteration
- Use `--verbose` flag to see detailed build information

## Usage

This example can be used as:
- A template for MIL-STD-498 compliant documentation
- A reference for automotive software documentation
- A training tool for requirements engineering
- A baseline for safety-critical system documentation

## Maintenance

All documents are maintained under configuration control with:
- Version history tracking
- Change management procedures
- Traceability matrix maintenance
- Regular review and update cycles

## Contributing

When contributing to this example:
1. Maintain MIL-STD-498 compliance
2. Update traceability relationships
3. Test builds before committing
4. Update this README if build procedures change
