
import re

Regex_Pattern = r'(\S{2}\s){2}\S{2}'

# Regex Pattern:
# XXxXXxXX
# ├── (\S{2}\s){2}
# │   ├── \S{2} - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ]) for 2 times
# │   ├── \s - Denotes any whitespace character (equal to [\r\n\t\f\v ])
# │   └── {2} - Denotes the above expression for 2 times
# └── \S{2}
#     ├── \S - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ]) for 2 times
#     └── {2} - Denotes the above expression twice

print(str(bool(re.search(Regex_Pattern, input()))).lower())