import base64
import hashlib

def attempt():
    print("Please enter the password to get the code:")
    password_attempt = input().strip()
    password = "aV9sb3ZlX215X2NhbmR5XzIwMjU="
    if base64.encodebytes(password_attempt.encode()).decode().strip() == password:
        print("You have entered the correct password.")
        print("The code for lock 2 is: " + hashlib.md5(password_attempt.encode()).hexdigest())
    else:
        print("You have entered the wrong password.")
        print("Exiting MOS")
        exit(1)
