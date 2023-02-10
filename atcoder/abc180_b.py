def minkowski_dist(x, p):
    ret = 0

    if p == float("inf"):
        for i in range(len(x)):
            ret = max(ret, abs(x[i]))
        return ret

    for i in range(len(x)):
        ret += abs((x[i]) ** p)

    return ret ** (1/p)

N = int(input())
x = list(map(int, input().split()))

print(minkowski_dist(x, 1))
print(minkowski_dist(x, 2))
print(minkowski_dist(x, float("inf")))
