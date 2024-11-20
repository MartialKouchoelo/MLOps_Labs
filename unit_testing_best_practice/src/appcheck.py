import re

def checkString(str):
    match = re.search(r'[a-zA-Z]+', str) and re.search(r'[0-9]+', str)
    if match:
        return True
    else:
        return False

def contains_special_characters(string):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    for char in string:
        if char in special_characters:
            return True
    return False

def func(username, password, email):
    res1 = " " in username
    res2 = "@" in email and "." in email
    if username == "" or res1:
        return False
    if len(password) < 8 or checkString(password) == False or contains_special_characters(password) == False:
        return False
    if not res2:
        return False
    return True