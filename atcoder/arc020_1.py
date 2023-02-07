A, B = map(abs, map(int, input().split()))
if A < B:
    print("Ant")
elif A > B:
    print("Bug")
else:
    print("Draw")