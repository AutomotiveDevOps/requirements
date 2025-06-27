#!/usr/bin/env python3
"""
/**
 * This code written by Claude Sonnet 4 (claude-3-5-sonnet-20241022)
 * Generated via Cursor IDE (cursor.sh) with AI assistance
 * Model: Anthropic Claude 3.5 Sonnet
 * Generation timestamp: 2024-12-19
 * Context: Improved script to fix StrictDoc files with proper RATIONALE field handling
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
            ('SPS-001', 'Project Scope', 'The project shall develop a comprehensive satellite communication management system with automated network control capabilities.', 'Project scope ensures clear understanding of deliverables and objectives.'),
            ('SPS-002', 'Project Objectives', 'The project shall deliver a secure, scalable, and reliable system that meets military communication standards.', 'Clear objectives ensure project success and stakeholder alignment.'),
            ('SPS-003', 'Project Timeline', 'The project shall be completed within 18 months with defined milestones and deliverables.', 'Timeline ensures project planning and resource allocation.'),
            ('SPS-004', 'Resource Requirements', 'The project shall require a team of 15 developers, 5 testers, and 3 system administrators.', 'Resource planning ensures adequate staffing for project success.'),
        ],
        'CPM': [
            ('CPM-001', 'Configuration Planning', 'The system shall implement comprehensive configuration management with version control and change tracking.', 'Configuration management ensures system consistency and traceability.'),
            ('CPM-002', 'Baseline Management', 'The system shall maintain configuration baselines for all software components and documentation.', 'Baseline management ensures system stability and change control.'),
            ('CPM-003', 'Change Control', 'The system shall implement formal change control procedures for all modifications and updates.', 'Change control ensures system integrity and risk management.'),
            ('CPM-004', 'Release Management', 'The system shall support automated release management with deployment pipelines and rollback capabilities.', 'Release management ensures reliable system deployment and updates.'),
        ],
        'DBDD': [
            ('DBDD-001', 'Database Design', 'The system shall use PostgreSQL database with normalized schema design and optimized queries.', 'Database design ensures data integrity and performance optimization.'),
            ('DBDD-002', 'Data Models', 'The system shall implement comprehensive data models for satellite configurations, network topology, and operational data.', 'Data models ensure proper data structure and relationships.'),
            ('DBDD-003', 'Data Integrity', 'The system shall enforce referential integrity, constraints, and validation rules for data consistency.', 'Data integrity ensures reliable and accurate data storage.'),
            ('DBDD-004', 'Performance Optimization', 'The system shall implement database indexing, query optimization, and connection pooling for optimal performance.', 'Performance optimization ensures system responsiveness and scalability.'),
        ],
        'IDD': [
            ('IDD-001', 'Interface Design', 'The system shall provide RESTful API interfaces for external system integration.', 'Interface design ensures system interoperability and integration capabilities.'),
            ('IDD-002', 'User Interface', 'The system shall provide web-based user interfaces with responsive design and accessibility features.', 'User interface ensures effective system operation and user experience.'),
            ('IDD-003', 'Data Interfaces', 'The system shall support multiple data formats including JSON, XML, and CSV for data exchange.', 'Data interfaces ensure flexible data exchange and system compatibility.'),
            ('IDD-004', 'Security Interfaces', 'The system shall implement secure authentication and authorization interfaces.', 'Security interfaces ensure system protection and access control.'),
        ],
        'SSS': [
            ('SSS-001', 'System Overview', 'The system shall provide comprehensive satellite communication management capabilities.', 'System overview ensures clear understanding of system purpose and scope.'),
            ('SSS-002', 'System Architecture', 'The system shall implement distributed microservices architecture with containerized deployment.', 'System architecture ensures scalability, maintainability, and operational flexibility.'),
            ('SSS-003', 'System Integration', 'The system shall integrate with existing satellite networks and ground control systems.', 'System integration ensures operational compatibility and data exchange.'),
            ('SSS-004', 'System Security', 'The system shall implement multi-layered security controls and compliance measures.', 'System security ensures protection against threats and compliance with standards.'),
        ],
        'STR': [
            ('STR-001', 'Test Strategy', 'The system shall undergo comprehensive testing including unit, integration, system, and acceptance testing.', 'Test strategy ensures system quality and reliability validation.'),
            ('STR-002', 'Test Environment', 'The system shall be tested in environments that simulate production conditions.', 'Test environment ensures realistic testing and problem identification.'),
            ('STR-003', 'Test Coverage', 'The system shall achieve minimum 90% code coverage and 100% requirement coverage.', 'Test coverage ensures comprehensive validation and quality assurance.'),
            ('STR-004', 'Test Automation', 'The system shall support automated testing with continuous integration and deployment.', 'Test automation ensures efficient testing and rapid feedback.'),
        ],
        'SUM': [
            ('SUM-001', 'System Summary', 'The system provides comprehensive satellite communication management with automated control capabilities.', 'System summary provides executive overview of system capabilities and benefits.'),
            ('SUM-002', 'Key Features', 'The system includes network management, security controls, monitoring, and user interface components.', 'Key features highlight system capabilities and value proposition.'),
            ('SUM-003', 'Technical Approach', 'The system uses modern technologies including microservices, containerization, and cloud deployment.', 'Technical approach ensures system scalability and operational efficiency.'),
            ('SUM-004', 'Benefits', 'The system provides improved efficiency, security, and reliability for satellite communication operations.', 'Benefits demonstrate system value and return on investment.'),
        ],
        'FSM': [
            ('FSM-001', 'Facility Requirements', 'The system shall operate in secure facilities with appropriate environmental controls.', 'Facility requirements ensure system reliability and environmental protection.'),
            ('FSM-002', 'Hardware Infrastructure', 'The system shall use enterprise-grade hardware with redundancy and failover capabilities.', 'Hardware infrastructure ensures system availability and performance.'),
            ('FSM-003', 'Network Infrastructure', 'The system shall operate on secure networks with appropriate segmentation and monitoring.', 'Network infrastructure ensures secure and reliable communication.'),
            ('FSM-004', 'Environmental Controls', 'The system shall operate in controlled environments with appropriate temperature and humidity controls.', 'Environmental controls ensure system stability and longevity.'),
        ],
        'SDP': [
            ('SDP-001', 'Development Process', 'The project shall follow agile development methodology with iterative delivery and continuous feedback.', 'Development process ensures efficient project execution and stakeholder engagement.'),
            ('SDP-002', 'Quality Assurance', 'The project shall implement comprehensive quality assurance processes including code reviews and testing.', 'Quality assurance ensures system reliability and stakeholder confidence.'),
            ('SDP-003', 'Risk Management', 'The project shall identify and mitigate risks through proactive planning and monitoring.', 'Risk management ensures project success and stakeholder protection.'),
            ('SDP-004', 'Communication Plan', 'The project shall maintain regular communication with stakeholders through status reports and meetings.', 'Communication plan ensures stakeholder alignment and project transparency.'),
        ],
        'SSDD': [
            ('SSDD-001', 'System Design Overview', 'The system shall implement distributed architecture with microservices and containerized deployment.', 'System design overview ensures architectural clarity and implementation guidance.'),
            ('SSDD-002', 'Component Design', 'The system shall include network management, security, user interface, and data management components.', 'Component design ensures modular architecture and maintainability.'),
            ('SSDD-003', 'Interface Design', 'The system shall provide RESTful APIs and web-based user interfaces.', 'Interface design ensures system interoperability and user accessibility.'),
            ('SSDD-004', 'Data Design', 'The system shall use PostgreSQL database with optimized schema and performance tuning.', 'Data design ensures efficient data storage and retrieval operations.'),
        ],
        'STD': [
            ('STD-001', 'Software Test Description', 'The system shall undergo comprehensive testing including functional, performance, and security testing.', 'Software test description ensures thorough validation and quality assurance.'),
            ('STD-002', 'Test Procedures', 'The system shall follow standardized test procedures with documented test cases and expected results.', 'Test procedures ensure consistent and reliable testing execution.'),
            ('STD-003', 'Test Data', 'The system shall use representative test data that simulates production conditions.', 'Test data ensures realistic testing and accurate problem identification.'),
            ('STD-004', 'Test Tools', 'The system shall use automated testing tools for efficient test execution and reporting.', 'Test tools ensure efficient testing and comprehensive coverage.'),
        ],
        'SVD': [
            ('SVD-001', 'Software Version Description', 'The system shall maintain version control with clear identification of software releases.', 'Software version description ensures configuration management and release tracking.'),
            ('SVD-002', 'Version Management', 'The system shall implement semantic versioning with major, minor, and patch version numbers.', 'Version management ensures clear release identification and change tracking.'),
            ('SVD-003', 'Release Notes', 'The system shall provide comprehensive release notes documenting changes and new features.', 'Release notes ensure stakeholder communication and change awareness.'),
            ('SVD-004', 'Deployment Instructions', 'The system shall provide clear deployment instructions for each software version.', 'Deployment instructions ensure reliable system installation and updates.'),
        ],
        'STRP': [
            ('STRP-001', 'Software Test Report', 'The system shall generate comprehensive test reports documenting test results and coverage.', 'Software test report ensures test transparency and stakeholder communication.'),
            ('STRP-002', 'Test Metrics', 'The system shall track and report test metrics including pass/fail rates and coverage statistics.', 'Test metrics ensure quality measurement and continuous improvement.'),
            ('STRP-003', 'Defect Tracking', 'The system shall track and manage defects through resolution and verification.', 'Defect tracking ensures problem resolution and quality improvement.'),
            ('STRP-004', 'Test Summary', 'The system shall provide executive summaries of test results and recommendations.', 'Test summary ensures stakeholder communication and decision support.'),
        ],
        'OCD': [
            ('OCD-001', 'Operator Manual', 'The system shall provide comprehensive operator documentation with procedures and troubleshooting guides.', 'Operator manual ensures effective system operation and problem resolution.'),
            ('OCD-002', 'User Training', 'The system shall include training materials and user guides for system operators.', 'User training ensures effective system utilization and user competence.'),
            ('OCD-003', 'Operational Procedures', 'The system shall document standard operating procedures for daily operations and maintenance.', 'Operational procedures ensure consistent and reliable system operation.'),
            ('OCD-004', 'Emergency Procedures', 'The system shall provide emergency procedures for system failures and incident response.', 'Emergency procedures ensure rapid incident response and system recovery.'),
        ],
    }
    
    # Get requirements for this document type
    requirements = requirements_map.get(file_stem, [
        (f'{file_stem}-001', 'General Requirement', 'The system shall meet the specified requirements for this document type.', 'This requirement ensures proper system functionality and compliance with standards.'),
        (f'{file_stem}-002', 'Document Compliance', 'The document shall comply with MIL-STD-498 standards and guidelines.', 'Document compliance ensures adherence to established standards and best practices.'),
        (f'{file_stem}-003', 'Quality Assurance', 'The document shall undergo review and approval processes to ensure quality.', 'Quality assurance ensures document accuracy and stakeholder confidence.'),
        (f'{file_stem}-004', 'Configuration Management', 'The document shall be maintained under configuration control with version tracking.', 'Configuration management ensures document consistency and change control.'),
    ])
    
    # Generate requirement blocks
    requirement_blocks = []
    for uid, title, statement, rationale in requirements:
        block = f"""[REQUIREMENT]
UID: {uid}
STATUS: Draft
TITLE: {title}
STATEMENT: {statement}
RATIONALE: {rationale}"""
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