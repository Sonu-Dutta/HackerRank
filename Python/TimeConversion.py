
def timeConversion(s):
    m=s[-2:]
    if m=='PM' and s[:2]!='12':
        s=str(12+int(s[:2]))+s[2:]
    if m=='AM' and s[:2]=='12':
        s='00' + s[2:]
    return s[:-2]
print(timeConversion("12:05:45 PM"))
print(timeConversion("12:05:45 AM"))
print(timeConversion("05:05:45 PM"))