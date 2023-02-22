K, A, B = map(int, input().split())

# 叩く以外の選択肢が無い、または叩いた方がオトク
if K < A+1 or A+2 >= B:
    print(K+1)
else:
    K -= A
    if K % 2 == 1:
        print((K+1)//2*B - K//2*A)
    else:
        print(K//2*(B-A)+A+1)
