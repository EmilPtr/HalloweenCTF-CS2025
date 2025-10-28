import hashlib

def check(identifier, password):
    if identifier == 1:
        if hashlib.md5(password.encode()).hexdigest() == "66e0d1846a8332461e649dc829d9a9da":
            return True
        else:
            return False
    if identifier == 2:
        if hashlib.md5(password.encode()).hexdigest() == "0f35e7f8ccd7f9661e644ca5695ccd6c":
            return True
        else:
            return False
    if identifier == 3:
        if hashlib.md5(password.encode()).hexdigest() == "fe2b13fcd21cdbb0160d15099e2b4d4b":
            return True
        else:
            return False
    if identifier == 4:
        if hashlib.md5(password.encode()).hexdigest() == "d557ba5ba8a86b042d661b813e7bc66e":
            return True
        else:
            return False
    else:
        return False