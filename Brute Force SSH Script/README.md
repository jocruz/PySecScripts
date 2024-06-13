```markdown
# SSH Brute Force Script 🚀

This repository contains an SSH brute force script that automates the process of testing common passwords against an SSH server to identify possible vulnerabilities. The script is developed using Python and leverages the `pwnlib` and `paramiko` libraries for handling SSH connections and managing exceptions.

## Script Overview 📄

The script attempts to authenticate to a specified SSH server using a list of common passwords. It is designed to demonstrate how automated testing can be applied in security assessments.

### Features:

- **Automated Password Testing**: Loops through a list of passwords, attempting to connect to an SSH server.
- **Connection Management**: Ensures that all SSH connections are properly closed after testing each password.
- **Immediate Feedback**: Provides real-time output on the success or failure of password attempts.
- **Secure Practices**: Highlights the importance of using strong, uncommon passwords to secure SSH servers.

## Prerequisites 📋

To run this script, you'll need:
- Python 3
- `pwnlib`
- `paramiko`

Ensure these are installed on your system by running:
```bash
pip install pwn paramiko
```

## How to Use the Script 🔧

1. Ensure the SSH server you intend to test is configured and running.
2. Modify the `host` and `username` variables in the script to match the target SSH server's details.
3. Run the script with Python:
```bash
python3 ssh_brute.py
```
