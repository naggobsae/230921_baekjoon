import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

word = sys.stdin.readline().rstrip()

for i in alphabet:
    print(word.find(i), end=' ')