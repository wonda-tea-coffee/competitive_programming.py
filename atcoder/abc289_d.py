import sys
import copy
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

mae = set()
mae.add(0)
all = set([0])
while True:
    tugi = set()
    c = 0
    for i in mae:
        for ai in A:
            if i+ai <= X and not i+ai in mae and not i+ai in B:
                tugi.add(i+ai)
                c += 1
    if c == 0: break
    mae = tugi
    all |= tugi

if X in all:
    print("Yes")
else:
    print("No")
