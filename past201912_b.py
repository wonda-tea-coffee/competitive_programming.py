N = int(input())
before = int(input())

for i in range(N-1):
    A = int(input())
    if A == before:
        print("stay")
    elif A > before:
        print("up", A-before)
    else:
        print("down", before-A)
    before = A
