X = int(input())
A = int(input())
B = int(input())

X -= A
X -= X//B*B
print(X)