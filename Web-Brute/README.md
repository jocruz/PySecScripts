# Brute Force Login Tester 🛡️

## Overview 🌐
This Python script automates the process of brute force testing on web login forms. It utilizes a list of common usernames and passwords to attempt to log in to a specified target URL.

## Features 🌟
- **Automated Login Attempts**: Cycles through a predefined list of usernames and passwords.
- **Immediate Feedback**: Prints attempt results in real-time, informing if a match is found.
- **Exit Upon Success**: Stops execution upon successful login detection, saving time and resources.

## Usage ⚙️
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Set up Environment**:
   ```bash
   pip install requests
   ```
3. **Run the Script**:
   ```bash
   python3 login_tester.py
   ```

## Configuration 📁
- **Target URL**: Modify the `target` variable to point to the URL you wish to test.
- **Usernames and Passwords**: Update the paths for `usernames_path` and `passwords` to your lists of usernames and passwords.
