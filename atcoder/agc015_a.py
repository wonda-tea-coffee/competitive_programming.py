N, A, B = map(int, input().split())

if A > B:
    print(0)
else:
    print(max(A+(N-1)*B-((N-1)*A+B)+1, 0))
