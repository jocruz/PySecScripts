# Import required libraries
from pwn import *  # Importing the pwn tools library for its useful utilities like log.progress
import sys  # Importing sys to handle command-line arguments

# Check if the correct number of command-line arguments have been passed
if len(sys.argv) != 2:
    print("Invalid arguments!")
    print("Usage: {} <sha256sum>".format(sys.argv[0]))  # Guide user on how to run the script
    exit()  # Exit the script if the number of arguments is incorrect

# The target SHA-256 hash we want to crack
wanted_hash = sys.argv[1]

# Path to the password file containing potential passwords
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0  # Initialize counter for the number of password attempts

# Start a progress logger to keep track of the brute force process
with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
    # Open the password file with the specified encoding
    with open(password_file, "r", encoding="latin-1") as password_list:
        # Iterate over each password in the file
        for password in password_list:
            password = password.strip("\n").encode("latin-1")  # Remove newline and encode to bytes

            # Calculate the SHA-256 hash of the password
            password_hash = sha256sumhex(password)

            # Update the progress status with the current attempt details
            p.status("[{}] {} == {}".format(
                attempts, password.decode("latin-1"), password_hash
            ))

            # Check if the computed hash matches the target hash
            if password_hash == wanted_hash:
                # If a match is found, log success and display the successful password and attempt count
                p.success(
                    "Password hash found after {} attempts! {} hashes to {}!".format(
                        attempts, password.decode("latin-1"), password_hash
                    )
                )
                exit()  # Exit the script upon successful cracking

            # Increment the attempt counter
            attempts += 1

        # Log failure if no matching hash was found after exhausting the password list
        p.failure("Password hash not found")
