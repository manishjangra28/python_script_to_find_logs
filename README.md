Detailed Overview of the Error Finder Script

Purpose
This Python script is designed to help developers, testers, and system administrators quickly identify and document error occurrences in log files or other text-based output. Its primary use cases include:

1: Error Tracking: Identifying recurring issues in application logs.
2: Debugging: Locating specific error messages during development or troubleshooting.
3: Quality Assurance: Automating part of the log analysis process in testing environments.
4: System Monitoring: Scanning system logs for known error patterns.

Functionality
The script performs the following operations:

1: File Reading: Opens and reads the contents of a specified text file.
2: String Matching: Searches for a user-specified substring throughout the file.
3: Line Number Tracking: Keeps track of line numbers where matches are found.
4: Console Output: Displays matching lines with their corresponding line numbers.
5: Log File Creation: Generates a new log file containing all findings.


Usage of the script:

run python log_finder.py
