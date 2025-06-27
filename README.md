# Requirements

Github actions example/template to automatically generate [`strictdoc`](https://github.com/strictdoc-project/strictdoc) documentation and publish it to GitHub pages.

Output: https://automotivedevops.github.io/requirements/

[![Requirements Publish](https://github.com/AutomotiveDevOps/requirements/actions/workflows/publish.yml/badge.svg)](https://github.com/AutomotiveDevOps/requirements/actions/workflows/publish.yml)

## MIL-STD-498 Documentation

This repository contains converted MIL-STD-498 documents from Markdown format to StrictDoc format (.sdoc files). The conversion maintains a 1:1 mapping of sections and preserves the original document structure.

### Generated Documentation

The following MIL-STD-498 documents have been successfully converted and are available in HTML format:

#### Core Documents
- [COM - Computer Operation Manual](docs/html/mil-std-498-strictdoc/COM.html)
- [CPM - Computer Programming Manual](docs/html/mil-std-498-strictdoc/CPM.html)
- [DBDD - Database Design Description](docs/html/mil-std-498-strictdoc/DBDD.html)
- [FSM - Functional Specification Manual](docs/html/mil-std-498-strictdoc/FSM.html)
- [IDD - Interface Design Description](docs/html/mil-std-498-strictdoc/IDD.html)
- [IRS - Interface Requirements Specification](docs/html/mil-std-498-strictdoc/IRS.html)
- [OCD - Operational Concept Document](docs/html/mil-std-498-strictdoc/OCD.html)

#### Software Development Documents
- [SCOM - Software Configuration Management Plan](docs/html/mil-std-498-strictdoc/SCOM.html)
- [SDD - Software Design Description](docs/html/mil-std-498-strictdoc/SDD.html)
- [SDP - Software Development Plan](docs/html/mil-std-498-strictdoc/SDP.html)
- [SPS - Software Product Specification](docs/html/mil-std-498-strictdoc/SPS.html)
- [SRS - Software Requirements Specification](docs/html/mil-std-498-strictdoc/SRS.html)
- [SSDD - Software System Design Description](docs/html/mil-std-498-strictdoc/SSDD.html)
- [SSS - System/Subsystem Specification](docs/html/mil-std-498-strictdoc/SSS.html)

#### Testing Documents
- [STD - Software Test Description](docs/html/mil-std-498-strictdoc/STD.html)
- [STP - Software Test Plan](docs/html/mil-std-498-strictdoc/STP.html)
- [STR - Software Test Report](docs/html/mil-std-498-strictdoc/STR.html)

#### Transition and User Documents
- [STRP - Software Transition Plan](docs/html/mil-std-498-strictdoc/STRP.html)
- [SUM - Software User Manual](docs/html/mil-std-498-strictdoc/SUM.html)
- [SVD - Software Version Description](docs/html/mil-std-498-strictdoc/SVD.html)

### Documentation Views

Each document is available in multiple views:
- **Main View**: Standard HTML documentation (e.g., `COM.html`)
- **Table View**: Requirements in table format (e.g., `COM-TABLE.html`)
- **Trace View**: Requirements with traceability links (e.g., `COM-TRACE.html`)
- **Deep Trace View**: Requirements with deep traceability analysis (e.g., `COM-DEEP-TRACE.html`)

## Git + Plain Text vs IBM DOORS Comparison

This repository includes comprehensive analysis documents demonstrating the superiority of Git + Plain Text workflows over IBM DOORS for requirements management in safety-critical systems.

### Core Analysis
- [**Git + Plain Text Superiority**](git_plain_text_superiority.md) - Executive overview of why Git + Plain Text is superior for requirements management, covering DO-178C and ISO 26262 compliance

### Detailed Comparisons

#### Cost Analysis
- [**Cost Comparison**](cost_comparison_doors_vs_git.md) - Comprehensive cost analysis showing **90% cost reduction** with Git + Plain Text, including TCO breakdown, ROI analysis, and risk assessment

#### User Experience
- [**User Experience Comparison**](user_experience_comparison_doors_vs_git.md) - Detailed UX analysis comparing learning curves (6-12 months vs 1-2 weeks), performance, collaboration, and user satisfaction metrics

#### Technical Capabilities
- [**Technical Comparison**](technical_comparison_doors_vs_git.md) - Architecture, performance, scalability, security, and integration analysis showing technical superiority of Git + Plain Text

#### Compliance and Safety
- [**Compliance Comparison**](compliance_comparison_doors_vs_git.md) - Regulatory compliance analysis covering DO-178C, ISO 26262, FDA, IEC 62304, and other safety standards

#### Migration Strategy
- [**Migration Guide**](migration_guide_doors_to_git.md) - Step-by-step migration strategy from IBM DOORS to Git + Plain Text, including planning, execution, validation, and best practices

### Key Findings

✅ **90% cost reduction** compared to IBM DOORS  
✅ **Superior performance** with faster, lighter tools  
✅ **Better user experience** with intuitive interfaces  
✅ **Enhanced compliance** with cryptographic audit trails  
✅ **Greater flexibility** with unlimited customization  
✅ **Future-proof** approach using open standards  
✅ **Immediate ROI** within 4 months  
✅ **Lower risk** profile with no vendor dependencies  

### Building the Documentation

To build the documentation locally:

```bash
make clean    # Clean all build artifacts
make venv     # Create Python virtual environment
make install  # Install dependencies
make docs     # Generate documentation
```

The generated documentation will be available in the `docs/html/` directory.

### Source Files

The original StrictDoc source files are located in the `mil-std-498-strictdoc/` directory. Each document follows the StrictDoc format with proper section structure and requirements numbering.
