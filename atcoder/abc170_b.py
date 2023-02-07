# a + b = X
# 2a + 4b = Y
#
# b = X - a
# 2a + 4(X - a) = Y
# -2a = Y - 4X
# a = (4X - Y)/2
X, Y = map(int, input().split())

a = (4*X - Y)/2
b = X - a
if a == int(a) and a >= 0 and b >= 0:
    print("Yes")
else:
    print("No")