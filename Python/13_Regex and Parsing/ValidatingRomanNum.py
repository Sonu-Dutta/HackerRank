
# Validating Roman Numerals in Python - Hacker Rank Solution
# Python 3
# Validating Roman Numerals in Python - Hacker Rank Solution START
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)	
# Do not delete 'r'.
# Validating Roman Numerals in Python - Hacker Rank Solution END

import re
print(str(bool(re.match(regex_pattern, input()))))