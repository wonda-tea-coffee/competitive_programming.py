import math

def minkowski_dist(x, y, p):
    assert len(x) == len(y)
    ret = 0

    if p == float("inf"):
        for i in range(len(x)):
            ret = max(ret, abs(x[i] - y[i]))
        return ret

    for i in range(len(x)):
        ret += abs((x[i] - y[i]) ** p)

    return ret ** (1/p)

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(minkowski_dist(x, y, 1))
print(minkowski_dist(x, y, 2))
print(minkowski_dist(x, y, 3))
print(minkowski_dist(x, y, float("inf")))
