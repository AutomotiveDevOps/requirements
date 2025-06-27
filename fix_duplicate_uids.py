#!/usr/bin/env python3
"""
Fix duplicate UIDs in .sdoc files by adding a suffix to example files.
This script adds '-EXAMPLE' suffix to all UIDs in examples/example1/ directory
to avoid conflicts with the main strictdoc/ directory.
"""

import os
import re
import glob

def fix_duplicate_uids():
    """Fix duplicate UIDs by adding suffix to example files."""
    example_dir = "examples/example1"
    
    # Find all .sdoc files in examples/example1/
    sdoc_files = glob.glob(f"{example_dir}/*.sdoc")
    
    for file_path in sdoc_files:
        print(f"Processing: {file_path}")
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace UID: XXX-XXX with UID: XXX-XXX-EXAMPLE
        # This regex matches UID: followed by any characters until end of line
        pattern = r'(UID:\s*[A-Z]+-\d+)'
        replacement = r'\1-EXAMPLE'
        
        # Apply the replacement
        new_content = re.sub(pattern, replacement, content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated UIDs in {file_path}")

if __name__ == "__main__":
    fix_duplicate_uids()
    print("Duplicate UID fix completed.") 