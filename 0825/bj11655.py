import sys

string = sys.stdin.readline().rstrip()

for i in string:
    if i.isupper():
        print(chr((ord(i) - 65 + 13) % 26 + 65), end='')
    elif i.islower():
        print(chr((ord(i) - 97 + 13) % 26 + 97), end='')
    else:
        print(i, end='')