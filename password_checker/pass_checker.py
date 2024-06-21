import requests
import hashlib
import sys
import os

def request_api_data(query_char):
    """
    Fetches data from the Pwned Passwords API for the given query characters.

    Parameters:
    query_char (str): The first five characters of the SHA-1 hashed password.

    Returns:
    Response: The response object from the API call.
    """
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data: {res.status_code}, try again!')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    """
    Checks the number of times a password hash has been leaked.

    Parameters:
    hashes (Response): The response object containing leaked password hashes.
    hash_to_check (str): The SHA-1 hashed tail of the password.

    Returns:
    int: The number of times the password hash was found leaked.
    """
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0

def pwned_api_check(password):
    """
    Checks if the given password has been leaked using the Pwned Passwords API.

    Parameters:
    password (str): The password to check.

    Returns:
    int: The number of times the password was found leaked.
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    """
    Main function to check if passwords have been leaked.

    Parameters:
    args (list): List of passwords to check.
    """
    if not args:
        print("Usage: python script.py <password1> <password2> ...")
        sys.exit(1)

    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password "{password}" was found {count} times. Please change your password.')
        else:
            print(f'Password "{password}" was NOT found. Carry on!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
