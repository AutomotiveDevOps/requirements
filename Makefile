# Makefile for local StrictDoc development
# Uses full escape for all variables as per user rules

.PHONY: help venv install clean docs reqif serve serve-milstd

# Default target
help:
	@echo "Available targets:"
	@echo "  venv     - Create Python virtual environment"
	@echo "  install  - Install dependencies in virtual environment"
	@echo "  docs     - Generate HTML documentation from all .sdoc files in the project"
	@echo "  reqif    - Generate ReqIF documentation from all .sdoc files in the project"
	@echo "  serve    - Serve generated documentation locally"
	@echo "  serve-milstd - Serve StrictDoc documentation locally"
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

# Generate HTML documentation
docs: install
	venv/bin/strictdoc export --output-dir docs/ $(shell find . -type f -name '*.sdoc' | grep -v './venv/' | grep -v './docs/')

# Generate ReqIF documentation
reqif: install
	venv/bin/strictdoc export --output-dir docs/ --formats reqif-sdoc $(shell find . -type f -name '*.sdoc' | grep -v './venv/' | grep -v './docs/')

# Generate both HTML and ReqIF documentation
all: install
	venv/bin/strictdoc export --output-dir docs/ --formats html,reqif-sdoc $(shell find . -type f -name '*.sdoc' | grep -v './venv/' | grep -v './docs/')

# Serve documentation locally (requires Python http.server)
serve: docs
	@echo "Serving documentation at http://localhost:8000"
	@echo "Generated files are in docs/html/"
	@echo "Press Ctrl+C to stop the server"
	cd docs/html && python3 -m http.server 8000

# Serve MIL-STD-498 documentation locally (requires Python http.server)
serve-milstd: docs
	@echo "Serving StrictDoc documentation at http://localhost:8001"
	@echo "StrictDoc files are in docs/html/strictdoc/"
	@echo "Press Ctrl+C to stop the server"
	cd docs/html/strictdoc && python3 -m http.server 8001

# Clean generated files and virtual environment
clean:
	rm -rf venv
	rm -rf docs/ 