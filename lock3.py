import base64
import hashlib

def attempt():
    print("Please enter the password to get the code:")
    password_attempt = list(input().strip())
    password_attempt_org = "".join(password_attempt)

    # I wonder if this is Base64...
    password = "c2NpX19zb3NnX2VydGEhXw=="

    if len(password_attempt) % 2 != 0:
        print("You have entered the wrong password.")
        print("Exiting MOS")
        exit(1)

    # Oh... it's some kind of shuffle...
    for x in range(0, int(len(password_attempt)), 2):
        temp = password_attempt[x]
        password_attempt[x] = password_attempt[x + 1]
        password_attempt[x + 1] = temp

    password_attempt = "".join(password_attempt)
    password_attempt = base64.encodebytes(password_attempt.encode()).decode().strip()

    if password == password_attempt:
        print("You have entered the correct password.")
        print("The code for lock 3 is: " + hashlib.md5(password_attempt_org.encode()).hexdigest())
    else:
        print("You have entered the wrong password.")
        print("Exiting MOS")
        exit(1)
