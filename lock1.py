import hashlib

def attempt():
    print("Please enter the password to get the code:")
    password_attempt = input()
    password = "happy_halloween_67"
    if password == password_attempt:
        print("You have entered the correct password.")
        print("The code for lock 1 is: " + hashlib.md5(password_attempt.encode()).hexdigest())
    else:
        print("You have entered the wrong password.")
        print("Exiting MOS")
        exit(1)