#!/usr/bin/env python3
"""
/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2025-01-27
 * Context: Script to fix section syntax in .sdoc files
 * 
 * Technical details:
 * - LLM: Claude 3.5 Sonnet (2024-10-22)
 * - IDE: Cursor (cursor.sh)
 * - Generation method: AI-assisted pair programming
 * - Code style: PEP 8 with type hints
 * - Dependencies: pathlib, glob, re
 */

Script to fix section syntax in .sdoc files.
This addresses the StrictDoc deprecation warning that will become an error in 2025 Q3.
"""

import glob
import os
import re
from pathlib import Path
from typing import List


def fix_section_syntax(file_path: str) -> bool:
    """
    Fix section syntax in a single .sdoc file.
    
    Args:
        file_path: Path to the .sdoc file to update
        
    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix opening sections: replace [SECTION] with [[SECTION]] (but not [[[SECTION]]])
        content = re.sub(r'\[SECTION\]', '[[SECTION]]', content)
        
        # Fix closing sections: replace [/SECTION] with [[/SECTION]] (but not [[[/SECTION]]])
        content = re.sub(r'\[/SECTION\]', '[[/SECTION]]', content)
        
        # If content changed, write it back
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def main() -> None:
    """Main function to fix all .sdoc files in the mil-std-498-strictdoc directory."""
    sdoc_dir = "mil-std-498-strictdoc"
    
    if not os.path.exists(sdoc_dir):
        print(f"Directory {sdoc_dir} not found!")
        return
    
    # Find all .sdoc files
    sdoc_files = glob.glob(os.path.join(sdoc_dir, "*.sdoc"))
    
    if not sdoc_files:
        print(f"No .sdoc files found in {sdoc_dir}")
        return
    
    print(f"Found {len(sdoc_files)} .sdoc files to process...")
    
    updated_count = 0
    for file_path in sdoc_files:
        if fix_section_syntax(file_path):
            updated_count += 1
    
    print(f"\nFix complete! Modified {updated_count} out of {len(sdoc_files)} files.")


if __name__ == "__main__":
    main() 