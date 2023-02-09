import sys

b = [
    set({7}),
    set({4}),
    set({8, 2}),
    set({5, 1}),
    set({9, 3}),
    set({6}),
    set({10})
]

S = input()

if S[0] == "1":
    print("No")
    sys.exit(0)

for i in range(10):
    if S[i] == "0":
        for bi in b:
            if i+1 in bi:
                bi.remove(i+1)
                break

# print(b)

for i in range(len(b)):
    if len(b[i]) == 0: continue

    for j in range(i+2, len(b)):
        if len(b[j]) == 0: continue

        for k in range(i+1, j):
            if len(b[k]) == 0:
                print("Yes")
                sys.exit(0)

print("No")
