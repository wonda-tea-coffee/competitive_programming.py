import sys

x, y = map(int, input().split())
for s in [{1, 3, 5, 7, 8, 10, 12}, {4, 6, 9, 11}, {2}]:
    if x in s and y in s:
        print("Yes")
        sys.exit(0)

print("No")
