Regex_Pattern = r'^\d{2,}[a-z]{0,}[A-Z]{0,}$'
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())