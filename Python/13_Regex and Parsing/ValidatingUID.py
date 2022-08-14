import re
for _ in range(int(input())):
    uid = input()
    uid = "".join(sorted(uid))
    if (re.search(r"[A-Z]{2}",uid) and #2 uppercase alphabets
        re.search(r"\d{3}",uid) and #3+ digits
        not re.search(r"[^A-Za-z0-9]",uid) and #no nonalphanumeric
        not re.search(r"(\w)\1",uid) and #no repetition
        len(uid) == 10): #10 characters long
        print("Valid")
    else:
        print("Invalid")