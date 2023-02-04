a, b, c = map(int, input().split())

def f(x):
    return a*x**5 + b*x + c

# f'(x)
def fp(x):
    return 5*a*x**4 + b

x = 2
log = set()
while True:
    x2 = x - f(x) / fp(x)
    if round(x2, 10) in log:
        print(x2)
        break
    log.add(round(x2, 10))
    x = x2
