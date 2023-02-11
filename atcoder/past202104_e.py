from collections import deque

N = int(input())
S = list(input())
A = deque([])

for i in range(N):
    if S[i] == "L":
        A.appendleft(i+1)
    elif S[i] == "R":
        A.append(i+1)
    elif S[i] == "A":
        if len(A) == 0:
            print("ERROR")
        else:
            print(A.popleft())
    elif S[i] == "B":
        if len(A) <= 1:
            print("ERROR")
        else:
            q = A.popleft()
            print(A.popleft())
            A.appendleft(q)
    elif S[i] == "C":
        if len(A) <= 2:
            print("ERROR")
        else:
            q1 = A.popleft()
            q2 = A.popleft()
            print(A.popleft())
            A.appendleft(q2)
            A.appendleft(q1)

    elif S[i] == "D":
        if len(A) == 0:
            print("ERROR")
        else:
            print(A.pop())
    elif S[i] == "E":
        if len(A) <= 1:
            print("ERROR")
        else:
            q = A.pop()
            print(A.pop())
            A.append(q)
    elif S[i] == "F":
        if len(A) <= 2:
            print("ERROR")
        else:
            q1 = A.pop()
            q2 = A.pop()
            print(A.pop())
            A.append(q2)
            A.append(q1)
