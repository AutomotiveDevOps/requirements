# Makefile for ADAS Control Module Example
# This Makefile uses the virtual environment and StrictDoc to build MIL-STD-498 documentation

# Virtual environment paths
VENV = ../../venv
PYTHON = ${VENV}/bin/python
STRICTDOC = ${VENV}/bin/strictdoc

# Project directories
PROJECT_ROOT = .
DOCS_DIR = docs
HTML_DIR = ${DOCS_DIR}/html

# Source files
SDOC_FILES = $(wildcard *.sdoc)

# Default target
all: ${HTML_DIR}/index.html

# Create virtual environment if it doesn't exist
${VENV}:
	cd ../.. && make venv

# Create documentation directories
${DOCS_DIR}:
	mkdir -p ${DOCS_DIR}

${HTML_DIR}: ${DOCS_DIR}
	mkdir -p ${HTML_DIR}

# Build HTML documentation
${HTML_DIR}/index.html: ${VENV} ${HTML_DIR} ${SDOC_FILES}
	${STRICTDOC} export --formats=html --output-dir=${HTML_DIR} ${PROJECT_ROOT}

# Build all documentation formats
docs: ${VENV} ${DOCS_DIR}
	${STRICTDOC} export --formats=html,markdown --output-dir=${DOCS_DIR} ${PROJECT_ROOT}

# Generate requirements traceability matrix
traceability: ${VENV}
	${STRICTDOC} export --formats=html --output-dir=${DOCS_DIR} --enable-mathjax --project-title="ADAS Control Module - Requirements Traceability" ${PROJECT_ROOT}

# Validate StrictDoc files
validate: ${VENV}
	${STRICTDOC} validate ${PROJECT_ROOT}

# Clean generated files
clean:
	rm -rf ${DOCS_DIR}

# Show help
help:
	@echo "Available targets:"
	@echo "  all          - Build HTML documentation (default)"
	@echo "  docs         - Build all documentation formats"
	@echo "  traceability - Generate requirements traceability matrix"
	@echo "  validate     - Validate StrictDoc files"
	@echo "  clean        - Remove generated documentation"
	@echo "  help         - Show this help message"

# Phony targets
.PHONY: all docs traceability validate clean help 