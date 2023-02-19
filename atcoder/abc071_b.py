S = set(input())

for i in range(97, 97+26):
    c = chr(i)
    if not c in S:
        print(c)
        exit()
print("None")
