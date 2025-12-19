Log File Analyser

The file analyser is a Python tool that processes "server logs" to detect suspicious activity, such as repeated failed login attempts. It is lightweight and easy to understand, only using Pythons standard library.

The project demonstrates:
* Log parsing and data aggregation
* Threshold-based detection
* Modular code organisation and clean function

Features:
* Parse log files line by line to efficiently handle large logs
* Extract IP addresses from log entries using regular expressions
* Count failed login attempts per IP address
* Flag suspicious IPs that exceed threshold
* Report Printed in console

Usage:
1. Place log file in project directory (default name: sample.log)
2. Run the program with Python 3
3. Output will display suspicious IPs exceeding the threshold

Security Considerations:
* Only failed login events counted, successful logins ignored
* Analyser uses simple threshold method, does not prevent attacks but detects behaviour

Extensibility:
* Add CLI arguments for threshold and log file path
* Detect activity within a time window
* Extend reports to other file types
* Add unit tests for all functions

Example Log Entry:
2025-01-12 05:11:03 FAILED_LOGIN ip=192.168.1.5 user=admin
2025-01-12 05:11:44 LOGIN_SUCCESS ip=192.168.1.5 user=admin


