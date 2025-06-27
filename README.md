# MIL-STD-498 Requirements Documentation

This repository contains comprehensive MIL-STD-498 documentation examples for safety-critical systems, including an Advanced Driver Assistance System (ADAS) Control Module and a Military Quad Copter RTOS.

## Overview

The repository demonstrates complete 1:1 mapping to the MIL-STD-498 standard document structure with:

- **Example 1**: ADAS Control Module - Complete automotive safety system
- **Example 2**: Military Quad Copter RTOS - Military-grade real-time system
- **StrictDoc Examples**: Official templates and reference documentation
- **Root Level**: Project documentation and test files

## 📖 View Documentation Online

### GitHub Pages Links

**Main Documentation Hub:**
- 🌐 [Documentation Navigation Hub](https://automotivedevops.github.io/requirements/)

**Example 1 - ADAS Control Module (Complete MIL-STD-498 Set):**
- 📋 [Software Requirements Specification (SRS)](https://automotivedevops.github.io/requirements/example1/html/SRS-TABLE.html)
- 🏗️ [Software Design Description (SDD)](https://automotivedevops.github.io/requirements/example1/html/SDD-TABLE.html)
- 🧪 [Software Test Plan (STP)](https://automotivedevops.github.io/requirements/example1/html/STP-TABLE.html)
- 📊 [Computer Operation Manual (COM)](https://automotivedevops.github.io/requirements/example1/html/COM-TABLE.html)
- 📋 [All Documents Index](https://automotivedevops.github.io/requirements/example1/html/index.html)

**Example 2 - Military Quad Copter RTOS:**
- 📋 [Software Requirements Specification (SRS)](https://automotivedevops.github.io/requirements/example2/html/SRS-TABLE.html)
- 🏗️ [Software Design Description (SDD)](https://automotivedevops.github.io/requirements/example2/html/SDD-TABLE.html)
- 🧪 [Software Test Plan (STP)](https://automotivedevops.github.io/requirements/example2/html/STP-TABLE.html)
- 📊 [All Documents Index](https://automotivedevops.github.io/requirements/example2/html/index.html)

**StrictDoc Examples & Templates:**
- 📋 [Minimal Example](https://automotivedevops.github.io/requirements/strictdoc/html/00_minimal-TABLE.html)
- 📋 [Minimal with Sections](https://automotivedevops.github.io/requirements/strictdoc/html/01_minimal_sections-TABLE.html)
- 📋 [Advanced Features](https://automotivedevops.github.io/requirements/strictdoc/html/02_advanced_features-TABLE.html)
- 📊 [All Documents Index](https://automotivedevops.github.io/requirements/strictdoc/html/index.html)

**Root Level Documentation:**
- 📋 [Bug Demo](https://automotivedevops.github.io/requirements/root/html/bug_demo-TABLE.html)
- 📋 [Test Files](https://automotivedevops.github.io/requirements/root/html/index.html)

## 🚀 Quick Start

### Option 1: View Online (Recommended)
All documentation is automatically generated and deployed to GitHub Pages. Simply click any of the links above to view the documentation in your browser.

### Option 2: Build Locally
To build the documentation locally:

```bash
# Clone the repository
git clone https://github.com/AutomotiveDevOps/requirements.git
cd requirements

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install strictdoc

# Build documentation for each directory
cd examples/example1
strictdoc export *.sdoc --output-dir docs --formats html --config strictdoc.toml

cd ../example2
strictdoc export *.sdoc --output-dir docs --formats html --config strictdoc.toml

cd ../../strictdoc
strictdoc export *.sdoc --output-dir docs --formats html --config strictdoc.toml

cd ..
strictdoc export *.sdoc --output-dir docs/root --formats html --config strictdoc.toml
```

### Option 3: Local Web Server
For the best experience, serve the files using a local web server:

```bash
# Using Python 3
cd docs
python3 -m http.server 8000

# Then open http://localhost:8000 in your browser
```

## 📋 MIL-STD-498 Document Set

This repository includes all 20 MIL-STD-498 document types with complete section and requirement mappings:

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

## 🔧 CI/CD Pipeline

The repository includes automated CI/CD pipelines that:

1. **Validate UID Uniqueness**: Ensures no duplicate UIDs across documents
2. **Grammar Validation**: Validates StrictDoc grammar compliance
3. **Documentation Generation**: Automatically builds HTML documentation
4. **GitHub Pages Deployment**: Deploys documentation to GitHub Pages

### Pre-commit Hooks
- UID uniqueness validation
- StrictDoc grammar validation
- Python code linting (ruff)
- YAML/JSON formatting (prettier)

## 📊 Requirements Coverage

The examples demonstrate comprehensive requirements coverage:

### Example 1 (ADAS Control Module)
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

### Example 2 (Military Quad Copter RTOS)
- Complete MIL-STD-498 document set for military-grade RTOS
- Real-time performance requirements
- Safety-critical system specifications
- Military compliance documentation

## 🏭 Automotive Context

Example 1 documents are tailored for automotive safety-critical applications with:
- ISO 26262 ASIL D compliance requirements
- MISRA C++ coding standards
- AUTOSAR architecture considerations
- Automotive communication protocols (CAN, FlexRay, Ethernet)
- Real-time performance requirements
- Environmental and safety constraints

## 🔗 Document Relationships

The documents maintain proper traceability relationships:
- SRS → SDD → Implementation
- SRS → STP → STD → STR/STRP
- OCD → SRS → SSS → SSDD
- IRS → IDD → Implementation
- SRS → SPS → SVD
- All documents → Configuration Management

## ✅ Quality Assurance

Each document includes:
- Unique requirement identifiers (UID)
- Clear requirement statements
- Rationale for each requirement
- Proper section hierarchy
- Traceability to related documents

## 🛡️ Compliance

This example demonstrates compliance with:
- MIL-STD-498 document structure requirements
- Automotive safety standards (ISO 26262)
- Software development best practices
- Requirements engineering principles
- Configuration management practices

## 🛠️ Troubleshooting

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

## 📚 Usage

This repository can be used as:
- A template for MIL-STD-498 compliant documentation
- A reference for automotive software documentation
- A training tool for requirements engineering
- A baseline for safety-critical system documentation

## 🔄 Maintenance

All documents are maintained under configuration control with:
- Version history tracking
- Change management procedures
- Traceability matrix maintenance
- Regular review and update cycles

## 🤝 Contributing

When contributing to this repository:
1. Maintain MIL-STD-498 compliance
2. Update traceability relationships
3. Test builds before committing
4. Update this README if build procedures change
5. Ensure UID uniqueness across all documents

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [StrictDoc Documentation](https://strictdoc.readthedocs.io/)
- [MIL-STD-498 Standard](https://en.wikipedia.org/wiki/MIL-STD-498)
- [ISO 26262 Automotive Safety](https://www.iso.org/standard/43464.html)
- [GitHub Repository](https://github.com/AutomotiveDevOps/requirements) 