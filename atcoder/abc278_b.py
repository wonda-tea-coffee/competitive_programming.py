def check(h, m):
    a = h//10*10 + m//10
    b = h%10*10 + m%10
    return a < 24 and b < 60

H, M = map(int, input().split())
for i in range(60*24):
    h = (H + (M+i) // 60) % 24
    m = (M + i % 60) % 60
    # print(h, m, i)
    if check(h, m):
        print(h, m)
        break
