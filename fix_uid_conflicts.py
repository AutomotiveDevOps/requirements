#!/usr/bin/env python3
"""
Fix UID conflicts in StrictDoc files.

This script ensures that each document has unique UIDs by prefixing them
with a document-specific identifier.
"""

import os
import re
import glob
from typing import Dict, List, Tuple
from pathlib import Path


def get_document_prefix(filename: str) -> str:
    """Generate a unique prefix for each document based on its name."""
    # Remove .sdoc extension and get base name
    base_name = os.path.splitext(os.path.basename(filename))[0]
    
    # Create a short prefix (2-3 characters)
    if base_name.startswith('SRS'):
        return 'SRS'
    elif base_name.startswith('SDD'):
        return 'SDD'
    elif base_name.startswith('STP'):
        return 'STP'
    elif base_name.startswith('STD'):
        return 'STD'
    elif base_name == 'STR':
        return 'STR'
    elif base_name == 'STRP':
        return 'STRP'  # Different prefix for STRP
    elif base_name.startswith('OCD'):
        return 'OCD'
    elif base_name.startswith('SSS'):
        return 'SSS'
    elif base_name.startswith('SSDD'):
        return 'SSDD'
    elif base_name.startswith('IRS'):
        return 'IRS'
    elif base_name.startswith('IDD'):
        return 'IDD'
    elif base_name.startswith('SPS'):
        return 'SPS'
    elif base_name.startswith('SVD'):
        return 'SVD'
    elif base_name.startswith('DBDD'):
        return 'DBDD'
    elif base_name.startswith('SUM'):
        return 'SUM'
    elif base_name.startswith('SDP'):
        return 'SDP'
    elif base_name.startswith('CPM'):
        return 'CPM'
    elif base_name.startswith('FSM'):
        return 'FSM'
    elif base_name.startswith('COM'):
        return 'COM'
    else:
        # For other files, use first 3 characters
        return base_name[:3].upper()


def fix_uid_conflicts_in_file(filepath: str) -> Tuple[int, List[str]]:
    """
    Fix UID conflicts in a single .sdoc file.
    
    Returns:
        Tuple of (number of changes made, list of old UIDs that were changed)
    """
    document_prefix = get_document_prefix(filepath)
    changes_made = 0
    changed_uids = []
    
    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all UID lines and replace them
    uid_pattern = r'^UID: REQ-(\d+)$'
    
    def replace_uid(match):
        nonlocal changes_made, changed_uids
        old_uid = match.group(0)
        req_number = match.group(1)
        new_uid = f'UID: {document_prefix}-{req_number}'
        changes_made += 1
        changed_uids.append(old_uid)
        return new_uid
    
    # Apply the replacement
    new_content = re.sub(uid_pattern, replace_uid, content, flags=re.MULTILINE)
    
    # Write back to file if changes were made
    if changes_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Fixed {changes_made} UIDs in {os.path.basename(filepath)}")
        for old_uid in changed_uids:
            print(f"    {old_uid} -> {old_uid.replace('REQ-', f'{document_prefix}-')}")
    
    return changes_made, changed_uids


def main():
    """Main function to fix UID conflicts across all .sdoc files."""
    print("🔧 Fixing UID conflicts in StrictDoc files...")
    
    # Find all .sdoc files
    sdoc_files = []
    for pattern in ['**/*.sdoc', '*.sdoc']:
        sdoc_files.extend(glob.glob(pattern, recursive=True))
    
    if not sdoc_files:
        print("❌ No .sdoc files found!")
        return
    
    print(f"📁 Found {len(sdoc_files)} .sdoc files")
    
    total_changes = 0
    total_files_changed = 0
    
    # Process each file
    for filepath in sorted(sdoc_files):
        print(f"\n📄 Processing: {filepath}")
        changes, changed_uids = fix_uid_conflicts_in_file(filepath)
        
        if changes > 0:
            total_changes += changes
            total_files_changed += 1
    
    print(f"\n✅ UID conflict fix completed!")
    print(f"📊 Summary:")
    print(f"   - Files processed: {len(sdoc_files)}")
    print(f"   - Files changed: {total_files_changed}")
    print(f"   - Total UIDs fixed: {total_changes}")
    
    if total_changes > 0:
        print(f"\n💡 All UIDs are now unique per document with prefixes like:")
        print(f"   - SRS-1, SRS-2, SRS-3... (Software Requirements Specification)")
        print(f"   - SDD-1, SDD-2, SDD-3... (Software Design Description)")
        print(f"   - STP-1, STP-2, STP-3... (Software Test Plan)")
        print(f"   - etc.")


if __name__ == "__main__":
    main() 