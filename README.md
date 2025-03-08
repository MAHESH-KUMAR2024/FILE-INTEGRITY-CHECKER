# FILE-INTEGRITY-CHECKER

#COMPANY#: CODTECH IT SOLUTIONS

#NAME#: MAHESH KUMAR P

#INTERN ID#: CT08SIK

#DOMAIN#: CYBER SECURITY & ETHICAL HACKING

#DURATION#: 4 WEEKS

#MENTOR#: NEELA SANTHOSH KUMAR

# DESCRIPTION #
# Task 1:#
#File Integrity Monitoring Tool
This tool monitors file changes by calculating and comparing SHA-256 hash values. It helps detect unauthorized modifications, additions, or deletions in a specified directory.
# Features Implemented#
•Scans a directory and computes hash values for all files.
•Detects file changes (added, modified, or deleted files).
•Compares current and previous hashes stored in a JSON file.
•Alerts the user if any changes are detected.
•Runs continuously to track real-time modifications.
# Libraries Used#
•hashlib → Generates SHA-256 hash values.
•os → Handles file and directory operations.
•json → Stores and retrieves file hashes for comparison.
•time → Introduces delays for continuous monitoring.
# How It Works#
•The script scans all files in the target directory.
•It computes SHA-256 hash values for each file.
•Compares the new hashes with stored values in file_hashes.json.
•If differences are found, it logs the changes and alerts the user.
•Updated hashes are saved for future comparisons.
# Outcome#
•A simple and effective tool for file integrity monitoring.
•Helps detect unauthorized file changes, malware activity, or corruption.
•Useful for security audits and forensic analysis.
