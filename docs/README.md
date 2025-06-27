# GitHub Pages Documentation

This directory contains the generated documentation for GitHub Pages deployment.

## Structure

- `index.html` - Main landing page for the repository
- `examples/example1/docs/html/` - Complete HTML documentation for Automotive ADAS example
- `examples/example2/docs/html/` - HTML documentation for Military Quad Copter RTOS example (when generated)

## Deployment

The documentation is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the main branch.

### Manual Deployment

To manually generate and deploy the documentation:

1. **Generate HTML for example1**:
   ```bash
   cd examples/example1
   strictdoc export . --output-dir docs --formats html
   ```

2. **Generate HTML for example2**:
   ```bash
   cd examples/example2
   strictdoc export . --output-dir docs --formats html
   ```

3. **Copy the main index.html** to the root of the repository

4. **Commit and push** the changes to trigger automatic deployment

## Accessing the Documentation

Once deployed, the documentation will be available at:
- `https://[username].github.io/[repository-name]/`
- `https://[username].github.io/[repository-name]/examples/example1/docs/html/index.html`
- `https://[username].github.io/[repository-name]/examples/example2/docs/html/index.html`

## Local Development

To view the documentation locally:

```bash
# Serve the entire repository
python -m http.server 8000

# Or serve just the docs directory
cd docs
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser. 