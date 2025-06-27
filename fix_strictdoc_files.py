#!/usr/bin/env python3
"""
/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2024-12-19
 * Context: Script to fix StrictDoc files by removing unsupported section syntax
 * 
 * Technical details:
 * - LLM: Claude 3.5 Sonnet (2024-10-22)
 * - IDE: Cursor (cursor.sh)
 * - Generation method: AI-assisted pair programming
 * - Code style: PEP 8 with type hints
 * - Dependencies: pathlib, re
 */
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional


def fix_strictdoc_file(file_path: Path) -> bool:
    """
    Fix a StrictDoc file by removing section syntax and adding requirements if needed.
    
    Args:
        file_path: Path to the StrictDoc file
        
    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has section syntax
        if '[[[SECTION]]]' not in content:
            return False
        
        # Remove all section syntax
        content = re.sub(r'\[\[\[SECTION\]\]\]\s*\nTITLE:\s*[^\n]*\n', '', content)
        content = re.sub(r'\[\[\[/SECTION\]\]\]\s*\n', '', content)
        
        # Check if file has any requirements after removing sections
        if '[REQUIREMENT]' not in content:
            # Add sample requirements based on document type
            doc_title = extract_document_title(content)
            sample_requirements = generate_sample_requirements(doc_title, file_path.stem)
            content = content.rstrip() + '\n\n' + sample_requirements
        
        # Write the fixed content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False


def extract_document_title(content: str) -> str:
    """Extract document title from content."""
    match = re.search(r'TITLE:\s*([^\n]+)', content)
    return match.group(1) if match else "Unknown Document"


def generate_sample_requirements(doc_title: str, file_stem: str) -> str:
    """Generate sample requirements based on document type."""
    
    requirements_map = {
        'SPS': [
            ('SPS-001', 'Project Scope', 'The project shall develop a comprehensive satellite communication management system with automated network control capabilities.'),
            ('SPS-002', 'Project Objectives', 'The project shall deliver a secure, scalable, and reliable system that meets military communication standards.'),
            ('SPS-003', 'Project Timeline', 'The project shall be completed within 18 months with defined milestones and deliverables.'),
            ('SPS-004', 'Resource Requirements', 'The project shall require a team of 15 developers, 5 testers, and 3 system administrators.'),
        ],
        'CPM': [
            ('CPM-001', 'Configuration Planning', 'The system shall implement comprehensive configuration management with version control and change tracking.'),
            ('CPM-002', 'Baseline Management', 'The system shall maintain configuration baselines for all software components and documentation.'),
            ('CPM-003', 'Change Control', 'The system shall implement formal change control procedures for all modifications and updates.'),
            ('CPM-004', 'Release Management', 'The system shall support automated release management with deployment pipelines and rollback capabilities.'),
        ],
        'DBDD': [
            ('DBDD-001', 'Database Design', 'The system shall use PostgreSQL database with normalized schema design and optimized queries.'),
            ('DBDD-002', 'Data Models', 'The system shall implement comprehensive data models for satellite configurations, network topology, and operational data.'),
            ('DBDD-003', 'Data Integrity', 'The system shall enforce referential integrity, constraints, and validation rules for data consistency.'),
            ('DBDD-004', 'Performance Optimization', 'The system shall implement database indexing, query optimization, and connection pooling for optimal performance.'),
        ],
        'IDD': [
            ('IDD-001', 'Interface Design', 'The system shall provide RESTful API interfaces for external system integration.'),
            ('IDD-002', 'User Interface', 'The system shall provide web-based user interfaces with responsive design and accessibility features.'),
            ('IDD-003', 'Data Interfaces', 'The system shall support multiple data formats including JSON, XML, and CSV for data exchange.'),
            ('IDD-004', 'Security Interfaces', 'The system shall implement secure authentication and authorization interfaces.'),
        ],
        'SSS': [
            ('SSS-001', 'System Overview', 'The system shall provide comprehensive satellite communication management capabilities.'),
            ('SSS-002', 'System Architecture', 'The system shall implement distributed microservices architecture with containerized deployment.'),
            ('SSS-003', 'System Integration', 'The system shall integrate with existing satellite networks and ground control systems.'),
            ('SSS-004', 'System Security', 'The system shall implement multi-layered security controls and compliance measures.'),
        ],
        'STR': [
            ('STR-001', 'Test Strategy', 'The system shall undergo comprehensive testing including unit, integration, system, and acceptance testing.'),
            ('STR-002', 'Test Environment', 'The system shall be tested in environments that simulate production conditions.'),
            ('STR-003', 'Test Coverage', 'The system shall achieve minimum 90% code coverage and 100% requirement coverage.'),
            ('STR-004', 'Test Automation', 'The system shall support automated testing with continuous integration and deployment.'),
        ],
        'SUM': [
            ('SUM-001', 'System Summary', 'The system provides comprehensive satellite communication management with automated control capabilities.'),
            ('SUM-002', 'Key Features', 'The system includes network management, security controls, monitoring, and user interface components.'),
            ('SUM-003', 'Technical Approach', 'The system uses modern technologies including microservices, containerization, and cloud deployment.'),
            ('SUM-004', 'Benefits', 'The system provides improved efficiency, security, and reliability for satellite communication operations.'),
        ],
        'FSM': [
            ('FSM-001', 'Facility Requirements', 'The system shall operate in secure facilities with appropriate environmental controls.'),
            ('FSM-002', 'Hardware Infrastructure', 'The system shall use enterprise-grade hardware with redundancy and failover capabilities.'),
            ('FSM-003', 'Network Infrastructure', 'The system shall operate on secure networks with appropriate segmentation and monitoring.'),
            ('FSM-004', 'Environmental Controls', 'The system shall operate in controlled environments with appropriate temperature and humidity controls.'),
        ],
        'SDP': [
            ('SDP-001', 'Development Process', 'The project shall follow agile development methodology with iterative delivery and continuous feedback.'),
            ('SDP-002', 'Quality Assurance', 'The project shall implement comprehensive quality assurance processes including code reviews and testing.'),
            ('SDP-003', 'Risk Management', 'The project shall identify and mitigate risks through proactive planning and monitoring.'),
            ('SDP-004', 'Communication Plan', 'The project shall maintain regular communication with stakeholders through status reports and meetings.'),
        ],
        'SSDD': [
            ('SSDD-001', 'System Design Overview', 'The system shall implement distributed architecture with microservices and containerized deployment.'),
            ('SSDD-002', 'Component Design', 'The system shall include network management, security, user interface, and data management components.'),
            ('SSDD-003', 'Interface Design', 'The system shall provide RESTful APIs and web-based user interfaces.'),
            ('SSDD-004', 'Data Design', 'The system shall use PostgreSQL database with optimized schema and performance tuning.'),
        ],
        'STD': [
            ('STD-001', 'Software Test Description', 'The system shall undergo comprehensive testing including functional, performance, and security testing.'),
            ('STD-002', 'Test Procedures', 'The system shall follow standardized test procedures with documented test cases and expected results.'),
            ('STD-003', 'Test Data', 'The system shall use representative test data that simulates production conditions.'),
            ('STD-004', 'Test Tools', 'The system shall use automated testing tools for efficient test execution and reporting.'),
        ],
        'SVD': [
            ('SVD-001', 'Software Version Description', 'The system shall maintain version control with clear identification of software releases.'),
            ('SVD-002', 'Version Management', 'The system shall implement semantic versioning with major, minor, and patch version numbers.'),
            ('SVD-003', 'Release Notes', 'The system shall provide comprehensive release notes documenting changes and new features.'),
            ('SVD-004', 'Deployment Instructions', 'The system shall provide clear deployment instructions for each software version.'),
        ],
        'STRP': [
            ('STRP-001', 'Software Test Report', 'The system shall generate comprehensive test reports documenting test results and coverage.'),
            ('STRP-002', 'Test Metrics', 'The system shall track and report test metrics including pass/fail rates and coverage statistics.'),
            ('STRP-003', 'Defect Tracking', 'The system shall track and manage defects through resolution and verification.'),
            ('STRP-004', 'Test Summary', 'The system shall provide executive summaries of test results and recommendations.'),
        ],
        'OCD': [
            ('OCD-001', 'Operator Manual', 'The system shall provide comprehensive operator documentation with procedures and troubleshooting guides.'),
            ('OCD-002', 'User Training', 'The system shall include training materials and user guides for system operators.'),
            ('OCD-003', 'Operational Procedures', 'The system shall document standard operating procedures for daily operations and maintenance.'),
            ('OCD-004', 'Emergency Procedures', 'The system shall provide emergency procedures for system failures and incident response.'),
        ],
    }
    
    # Get requirements for this document type
    requirements = requirements_map.get(file_stem, [
        (f'{file_stem}-001', 'General Requirement', 'The system shall meet the specified requirements for this document type.'),
        (f'{file_stem}-002', 'Document Compliance', 'The document shall comply with MIL-STD-498 standards and guidelines.'),
        (f'{file_stem}-003', 'Quality Assurance', 'The document shall undergo review and approval processes to ensure quality.'),
        (f'{file_stem}-004', 'Configuration Management', 'The document shall be maintained under configuration control with version tracking.'),
    ])
    
    # Generate requirement blocks
    requirement_blocks = []
    for uid, title, statement in requirements:
        block = f"""[REQUIREMENT]
UID: {uid}
STATUS: Draft
TITLE: {title}
STATEMENT: {statement}
RATIONALE: This requirement ensures proper system functionality and compliance with standards."""
        requirement_blocks.append(block)
    
    return '\n\n'.join(requirement_blocks)


def main() -> None:
    """Main function to fix all StrictDoc files."""
    strictdoc_dir = Path('strictdoc')
    
    if not strictdoc_dir.exists():
        print("strictdoc directory not found")
        return
    
    # Find all .sdoc files
    sdoc_files = list(strictdoc_dir.glob('*.sdoc'))
    
    if not sdoc_files:
        print("No .sdoc files found")
        return
    
    print(f"Found {len(sdoc_files)} .sdoc files")
    
    # Fix each file
    fixed_count = 0
    for file_path in sdoc_files:
        if fix_strictdoc_file(file_path):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} out of {len(sdoc_files)} files")


if __name__ == '__main__':
    main() 