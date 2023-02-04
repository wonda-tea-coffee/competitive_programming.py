st = list(input())
q = int(input())

for _ in range(q):
    query = input().split()
    t = query[0]
    # print(st, "".join(st))
    if t == "print":
        a, b = map(int, query[1:])
        print("".join(st[a:b+1]))
    elif t == "reverse":
        a, b = map(int, query[1:])
        # print(a, b)
        rev = st[a:b+1]
        # print(rev)
        rev.reverse()
        # print(rev)
        st = st[:a] + rev + st[b+1:]
    else:
        a = int(query[1])
        b = int(query[2])
        p = query[3]
        st[a:b+1] = list(p)
