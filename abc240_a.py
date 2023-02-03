a, b = map(lambda x: int(x)%10, input().split())

if (a+1)%10==b or (a-1)%10==b:
    print("Yes")
else:
    print("No")