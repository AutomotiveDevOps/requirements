#!/usr/bin/env python3
"""
/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2025-01-27
 * Context: Script to update deprecated [SECTION] syntax to [[SECTION]] in .sdoc files
 * 
 * Technical details:
 * - LLM: Claude 3.5 Sonnet (2024-10-22)
 * - IDE: Cursor (cursor.sh)
 * - Generation method: AI-assisted pair programming
 * - Code style: PEP 8 with type hints
 * - Dependencies: pathlib, glob
 */

Script to update deprecated [SECTION] syntax to [[SECTION]] in .sdoc files.
This addresses the StrictDoc deprecation warning that will become an error in 2025 Q3.
"""

import glob
import os
from pathlib import Path
from typing import List


def update_section_syntax(file_path: str) -> bool:
    """
    Update a single .sdoc file to use the new [[SECTION]] syntax.
    
    Args:
        file_path: Path to the .sdoc file to update
        
    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file needs updating
        if '[SECTION]' not in content and '[/SECTION]' not in content:
            return False
        
        # Replace [SECTION] with [[SECTION]]
        updated_content = content.replace('[SECTION]', '[[SECTION]]')
        # Replace [/SECTION] with [[/SECTION]]
        updated_content = updated_content.replace('[/SECTION]', '[[/SECTION]]')
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Updated: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def main() -> None:
    """Main function to update all .sdoc files in the mil-std-498-strictdoc directory."""
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
        if update_section_syntax(file_path):
            updated_count += 1
    
    print(f"\nUpdate complete! Modified {updated_count} out of {len(sdoc_files)} files.")


if __name__ == "__main__":
    main() 