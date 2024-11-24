import sys
import re

print("Give the inputs:" , end="")

lines = sys.stdin.readlines()  # Read all lines until EOF

for line in lines:
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    fin_line = re.sub(r'\s+', ' ', line.strip())
    print(fin_line)  # Print the processed line
