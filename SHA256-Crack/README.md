# PySecScripts 🛡️

Welcome to **PySecScripts**, a collection of Python scripts designed for security testing and penetration testing. This repository showcases my skills in developing tools that automate security assessments and enhance network defense capabilities. 

## Current Project 🚀

### SSH Brute Force Script 🔐
- **Description**: This script attempts to crack a given SHA-256 hash by comparing it with hashes of passwords from the `rockyou.txt` wordlist.
- **Usage**: 
  - Ensure you have Python 3 installed.
  - Install required libraries: `pip install pwntools`
  - Run the script: `python sha256-crack.py <sha256sum>`
- **Features**:
  - Reads passwords from a file and encodes them.
  - Hashes each password using SHA-256.
  - Compares each hash with the target hash to find a match.
  - Provides real-time progress updates.


## Usage Instructions 🛠️

To run the current SSH Brute Force script:
```bash
python sha256-crack.py <sha256sum>
```
Replace `<sha256sum>` with the SHA-256 hash you want to crack.

---

