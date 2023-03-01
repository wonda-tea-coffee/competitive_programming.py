import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

# math.ceil(a*i/m)(i=1,2,...,n)の総和
def f(n, a, m):
	# print("(n, a, m) = (%d, %d, %d)" % (n, a, m))
	g = lcm(a, m)//a
	# print("g = %d" % g)
	h = lcm(a, m)//m
	# print("h = %d" % h)
	k = n // g
	# print("k = %d" % k)

	c = 0
	for i in range(1, g+1):
		c += math.ceil(a*i/m)
	# print("c = %d" % c)

	ret = k*c + h*g*(k-1)*k//2
	for i in range(n//g*g+1, n+1):
		# print("i=", i)
		ret += math.ceil(a*i/m)

	return ret

def g(n, a, m):
    ret = 0
    for i in range(1, n+1):
        ret += math.ceil(a*i/m)
    return ret

T = int(input())
for _ in range(T):
    N, A, M = map(int, input().split())
    # print(f(N, A, M), g(N, A, M))
    print(M*f(N, A, M) - A*N*(N+1)//2)

# print(f(14, 7, 8))
# print(g(14, 7, 8))
