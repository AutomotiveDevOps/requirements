#!/usr/bin/env python3
"""
StrictDoc Grammar Validator for Pre-commit Hooks

This script validates .sdoc files for correct grammar, structure, and common issues.
It's designed to be used as a pre-commit hook to ensure all .sdoc files are valid
before being committed to the repository.

Usage:
    python scripts/validate_strictdoc.py file1.sdoc file2.sdoc ...
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict, Optional
import argparse


class StrictDocValidator:
    """Validates StrictDoc (.sdoc) files for grammar and structure correctness."""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def validate_file(self, filepath: str) -> bool:
        """Validate a single .sdoc file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(filepath)
            print(f"🔍 Validating: {filename}")
            
            # Reset errors/warnings for this file
            self.errors = []
            self.warnings = []
            
            # Perform all validations
            self._validate_basic_structure(content, filename)
            self._validate_document_header(content, filename)
            self._validate_requirement_blocks(content, filename)
            self._validate_uid_uniqueness(content, filename)
            self._validate_field_order(content, filename)
            self._validate_blank_lines(content, filename)
            self._validate_section_structure(content, filename)
            
            # Report results
            if self.errors:
                print(f"❌ {filename}: {len(self.errors)} errors found")
                for error in self.errors:
                    print(f"   ERROR: {error}")
                return False
            elif self.warnings:
                print(f"⚠️  {filename}: {len(self.warnings)} warnings found")
                for warning in self.warnings:
                    print(f"   WARNING: {warning}")
                return True
            else:
                print(f"✅ {filename}: Valid")
                return True
                
        except Exception as e:
            print(f"❌ {filepath}: Failed to read file - {e}")
            return False
    
    def _validate_basic_structure(self, content: str, filename: str) -> None:
        """Validate basic file structure."""
        lines = content.split('\n')
        
        # Check for empty file
        if not content.strip():
            self.errors.append("File is empty")
            return
        
        # Check for [DOCUMENT] tag
        if '[DOCUMENT]' not in content:
            self.errors.append("Missing [DOCUMENT] tag")
        
        # Check for TITLE field
        if 'TITLE:' not in content:
            self.errors.append("Missing TITLE field")
        
        # Check for [REQUIREMENT] blocks
        if '[REQUIREMENT]' not in content:
            self.errors.append("No [REQUIREMENT] blocks found")
    
    def _validate_document_header(self, content: str, filename: str) -> None:
        """Validate document header structure."""
        lines = content.split('\n')
        
        # Find [DOCUMENT] and TITLE
        doc_index = -1
        title_index = -1
        
        for i, line in enumerate(lines):
            if line.strip() == '[DOCUMENT]':
                doc_index = i
            elif line.strip().startswith('TITLE:'):
                title_index = i
        
        # Check order: [DOCUMENT] should come before TITLE
        if doc_index != -1 and title_index != -1:
            if title_index <= doc_index:
                self.errors.append("TITLE field must come after [DOCUMENT] tag")
            
            # Check for blank line after TITLE (but make it a warning, not error)
            if title_index + 1 < len(lines):
                next_line = lines[title_index + 1].strip()
                if next_line and not next_line.startswith('[REQUIREMENT]'):
                    self.warnings.append("Consider adding blank line after TITLE field")
    
    def _validate_requirement_blocks(self, content: str, filename: str) -> None:
        """Validate [REQUIREMENT] block structure."""
        requirement_blocks = re.findall(r'\[REQUIREMENT\](.*?)(?=\[REQUIREMENT\]|$)', 
                                       content, re.DOTALL)
        
        for i, block in enumerate(requirement_blocks):
            block_lines = block.strip().split('\n')
            
            # Check for required fields
            required_fields = ['UID:', 'STATUS:', 'TITLE:', 'STATEMENT:', 'RATIONALE:']
            found_fields = []
            
            for line in block_lines:
                line = line.strip()
                for field in required_fields:
                    if line.startswith(field):
                        found_fields.append(field)
                        break
            
            # Check for missing required fields
            missing_fields = [field for field in required_fields if field not in found_fields]
            if missing_fields:
                self.errors.append(f"Requirement block {i+1} missing required fields: {', '.join(missing_fields)}")
            
            # Check field order (UID, STATUS, TAGS, TITLE, STATEMENT, RATIONALE)
            expected_order = ['UID:', 'STATUS:', 'TAGS:', 'TITLE:', 'STATEMENT:', 'RATIONALE:']
            actual_order = []
            
            for line in block_lines:
                line = line.strip()
                for field in expected_order:
                    if line.startswith(field):
                        actual_order.append(field)
                        break
            
            # Check if order is correct (allowing TAGS to be optional)
            if actual_order:
                # Remove TAGS from expected order for comparison
                expected_without_tags = [f for f in expected_order if f != 'TAGS:']
                actual_without_tags = [f for f in actual_order if f != 'TAGS:']
                
                if actual_without_tags != expected_without_tags:
                    self.errors.append(f"Requirement block {i+1} has incorrect field order. Expected: {', '.join(expected_without_tags)}")
    
    def _validate_uid_uniqueness(self, content: str, filename: str) -> None:
        """Validate UID uniqueness within the file."""
        uids = re.findall(r'UID:\s*([^\n]+)', content)
        uid_counts = {}
        
        for uid in uids:
            uid = uid.strip()
            uid_counts[uid] = uid_counts.get(uid, 0) + 1
        
        # Check for duplicate UIDs
        duplicates = [uid for uid, count in uid_counts.items() if count > 1]
        if duplicates:
            self.errors.append(f"Duplicate UIDs found: {', '.join(duplicates)}")
        
        # Check UID format
        for uid in uids:
            uid = uid.strip()
            if not re.match(r'^[A-Z]+-\d+$', uid):
                self.warnings.append(f"UID '{uid}' doesn't follow expected format (e.g., SRS-1, SDD-2)")
    
    def _validate_field_order(self, content: str, filename: str) -> None:
        """Validate field order within requirement blocks."""
        requirement_blocks = re.findall(r'\[REQUIREMENT\](.*?)(?=\[REQUIREMENT\]|$)', 
                                       content, re.DOTALL)
        
        for i, block in enumerate(requirement_blocks):
            lines = [line.strip() for line in block.split('\n') if line.strip()]
            
            # Find field positions
            field_positions = {}
            for j, line in enumerate(lines):
                for field in ['UID:', 'STATUS:', 'TAGS:', 'TITLE:', 'STATEMENT:', 'RATIONALE:']:
                    if line.startswith(field):
                        field_positions[field] = j
                        break
            
            # Check order
            expected_order = ['UID:', 'STATUS:', 'TAGS:', 'TITLE:', 'STATEMENT:', 'RATIONALE:']
            actual_order = [field for field in expected_order if field in field_positions]
            
            # Verify order
            for j in range(len(actual_order) - 1):
                current_field = actual_order[j]
                next_field = actual_order[j + 1]
                if field_positions[current_field] > field_positions[next_field]:
                    self.errors.append(f"Requirement block {i+1}: {current_field} comes after {next_field}")
    
    def _validate_blank_lines(self, content: str, filename: str) -> None:
        """Validate blank line usage."""
        lines = content.split('\n')
        
        # Check for blank lines between requirement blocks
        in_requirement = False
        for i, line in enumerate(lines):
            if line.strip() == '[REQUIREMENT]':
                in_requirement = True
                continue
            elif line.strip() == '[DOCUMENT]':
                in_requirement = False
                continue
            
            # Only check for blank lines between different requirement blocks
            # Not between fields within a requirement block
            if in_requirement and line.strip() == '[REQUIREMENT]':
                # Check if there's a blank line before this new requirement block
                if i > 0 and lines[i-1].strip():
                    self.warnings.append(f"Line {i+1}: Consider adding blank line between requirement blocks")
    
    def _validate_section_structure(self, content: str, filename: str) -> None:
        """Validate section structure if present."""
        # Check for proper section tags
        if '[[SECTION]]' in content:
            self.warnings.append("Uses [[SECTION]] tags - consider using [REQUIREMENT] blocks instead")
        
        # Check for balanced section tags
        section_open = content.count('[[SECTION]]')
        section_close = content.count('[[/SECTION]]')
        
        if section_open != section_close:
            self.errors.append(f"Unbalanced section tags: {section_open} opening, {section_close} closing")


def main():
    """Main function for the StrictDoc validator."""
    parser = argparse.ArgumentParser(description='Validate StrictDoc (.sdoc) files')
    parser.add_argument('files', nargs='+', help='.sdoc files to validate')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    validator = StrictDocValidator()
    all_valid = True
    
    print("🔧 StrictDoc Grammar Validator")
    print("=" * 50)
    
    for filepath in args.files:
        if not filepath.endswith('.sdoc'):
            print(f"⚠️  Skipping {filepath}: not a .sdoc file")
            continue
        
        if not os.path.exists(filepath):
            print(f"❌ {filepath}: file not found")
            all_valid = False
            continue
        
        if not validator.validate_file(filepath):
            all_valid = False
    
    print("=" * 50)
    if all_valid:
        print("✅ All files are valid!")
        sys.exit(0)
    else:
        print("❌ Validation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main() 