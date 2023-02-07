N = int(input())
for i in range(1, 10):
    if (i-1)*111 <= N <= i*111:
        print(i*111)
        break
