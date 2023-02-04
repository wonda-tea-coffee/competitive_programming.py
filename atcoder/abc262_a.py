Y = int(input())

if Y%4 == 0:
    Y += 2
elif Y%4 == 1:
    Y += 1
elif Y%4 == 2:
    pass
else:
    Y += 3

print(Y)
