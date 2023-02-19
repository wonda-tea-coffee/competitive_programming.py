N, A, B = map(int, input().split())
S = input()

passed = 0
ab = 0
for i in range(N):
    if S[i] == "a":
        if passed < A+B:
            print("Yes")
            passed += 1
        else:
            print("No")
    elif S[i] == "b":
        ab += 1
        if passed < A+B and ab <= B:
            print("Yes")
            passed += 1
        else:
            print("No")
    else:
        print("No")
