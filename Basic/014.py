line_count = 0
print("Give the inputs: ")
try:
    while True:
        line = input()
        line_count += 1
except EOFError:
    pass

print("Number of lines:", max(0, line_count-1))
