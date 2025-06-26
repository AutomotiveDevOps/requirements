# Makefile for local StrictDoc development
# Uses full escape for all variables as per user rules

.PHONY: help venv install clean docs serve serve-milstd

# Default target
help:
	@echo "Available targets:"
	@echo "  venv     - Create Python virtual environment"
	@echo "  install  - Install dependencies in virtual environment"
	@echo "  docs     - Generate documentation from .sdoc files"
	@echo "  serve    - Serve generated documentation locally"
	@echo "  serve-milstd - Serve MIL-STD-498 documentation locally"
	@echo "  clean    - Clean generated files and virtual environment"

# Create virtual environment
venv:
	python3 -m venv venv

# Install dependencies
install: venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install strictdoc
	venv/bin/pip install toml
	venv/bin/pip install pygments

# Generate documentation
docs: install
	venv/bin/strictdoc export --output-dir docs/ mil-std-498-strictdoc/*.sdoc

# Serve documentation locally (requires Python http.server)
serve: docs
	@echo "Serving documentation at http://localhost:8000"
	@echo "Generated files are in docs/html/"
	@echo "Press Ctrl+C to stop the server"
	cd docs/html && python3 -m http.server 8000

# Serve MIL-STD-498 documentation locally (requires Python http.server)
serve-milstd: docs
	@echo "Serving MIL-STD-498 documentation at http://localhost:8001"
	@echo "MIL-STD files are in docs/html/mil-std-498-strictdoc/"
	@echo "Press Ctrl+C to stop the server"
	cd docs/html/mil-std-498-strictdoc && python3 -m http.server 8001

# Clean generated files and virtual environment
clean:
	rm -rf venv
	rm -rf docs/ 