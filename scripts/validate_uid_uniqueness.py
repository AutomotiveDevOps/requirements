#!/usr/bin/env python3
"""
UID Uniqueness Validator for Pre-commit Hooks

This script validates that all UIDs across all .sdoc files in the repository
are completely unique. It's designed to be used as a pre-commit hook to prevent
UID conflicts before they reach CI/CD.

Usage:
    python scripts/validate_uid_uniqueness.py
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict


class UIDUniquenessValidator:
    """Validates UID uniqueness across all .sdoc files."""
    
    def __init__(self):
        self.all_uids: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.conflicts: List[str] = []
        
    def find_sdoc_files(self, root_dir: str = ".") -> List[str]:
        """Find all .sdoc files in the repository."""
        sdoc_files = []
        for root, dirs, files in os.walk(root_dir):
            # Skip virtual environment and build directories
            dirs[:] = [d for d in dirs if d not in ['venv', '.venv', '__pycache__', '.git', 'build', 'dist', 'docs', 'html_demo', 'html_sum_test', 'MIL-STD-498', 'strictdoc', 'examples/example1/docs', 'examples/example2/docs', 'examples/example1/test_build', 'examples/example2/test_build']]
            
            for file in files:
                if file.endswith('.sdoc'):
                    sdoc_files.append(os.path.join(root, file))
        
        return sorted(sdoc_files)
    
    def extract_uids_from_file(self, filepath: str) -> List[Tuple[str, int]]:
        """Extract all UIDs from a single .sdoc file with line numbers."""
        uids = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line.startswith('UID:'):
                        uid_match = re.search(r'UID:\s*([^\n]+)', line)
                        if uid_match:
                            uid = uid_match.group(1).strip()
                            uids.append((uid, line_num))
        except Exception as e:
            print(f"❌ Error reading {filepath}: {e}")
        
        return uids
    
    def validate_file(self, filepath: str) -> None:
        """Validate UIDs in a single file and collect them."""
        filename = os.path.basename(filepath)
        print(f"🔍 Checking UIDs in: {filename}")
        
        uids = self.extract_uids_from_file(filepath)
        
        # Check for duplicate UIDs within the same file
        uid_counts = defaultdict(list)
        for uid, line_num in uids:
            uid_counts[uid].append(line_num)
        
        for uid, line_nums in uid_counts.items():
            if len(line_nums) > 1:
                self.conflicts.append(f"❌ {filename}: Duplicate UID '{uid}' on lines {line_nums}")
            else:
                # Add to global collection for cross-file checking
                self.all_uids[uid].append((filepath, line_nums[0]))
    
    def check_cross_file_conflicts(self) -> None:
        """Check for UID conflicts across different files."""
        for uid, locations in self.all_uids.items():
            if len(locations) > 1:
                # Group by filepath to avoid duplicate file entries
                file_groups = defaultdict(list)
                for filepath, line_num in locations:
                    file_groups[filepath].append(line_num)
                
                # Create a clean list of file:line entries
                file_list = []
                for filepath, line_nums in file_groups.items():
                    filename = os.path.basename(filepath)
                    if len(line_nums) == 1:
                        file_list.append(f"{filename}:{line_nums[0]}")
                    else:
                        file_list.append(f"{filename}:{line_nums}")
                
                self.conflicts.append(f"❌ UID '{uid}' found in multiple files: {', '.join(file_list)}")
    
    def validate_all(self) -> bool:
        """Validate UID uniqueness across all .sdoc files."""
        print("🔧 UID Uniqueness Validator")
        print("=" * 50)
        
        # Find all .sdoc files
        sdoc_files = self.find_sdoc_files()
        print(f"📁 Found {len(sdoc_files)} .sdoc files")
        
        if not sdoc_files:
            print("⚠️  No .sdoc files found")
            return True
        
        # Validate each file
        for filepath in sdoc_files:
            self.validate_file(filepath)
        
        # Check for cross-file conflicts
        print("\n🔍 Checking for cross-file UID conflicts...")
        self.check_cross_file_conflicts()
        
        # Report results
        print("\n" + "=" * 50)
        
        if self.conflicts:
            print(f"❌ Found {len(self.conflicts)} UID conflicts:")
            for conflict in self.conflicts:
                print(f"   {conflict}")
            return False
        else:
            print("✅ All UIDs are unique across all .sdoc files!")
            return True


def main():
    """Main function for the UID uniqueness validator."""
    validator = UIDUniquenessValidator()
    
    if not validator.validate_all():
        print("\n❌ UID uniqueness validation failed!")
        print("Please fix the conflicts before committing.")
        sys.exit(1)
    else:
        print("\n✅ UID uniqueness validation passed!")
        sys.exit(0)


if __name__ == "__main__":
    main() 