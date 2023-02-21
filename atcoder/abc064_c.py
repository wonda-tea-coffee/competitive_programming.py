N = int(input())
a = list(map(int, input().split()))
pro = 0
color = [False]*8

for ai in a:
    if ai >= 3200:
        pro += 1
    else:
        color[ai//400] = True

# print(color)
c = sum(map(lambda x: 1 if x else 0, color))
print(max(c, 1), c+pro)
