N = int(input())
st = []
for _ in range(N):
    s, t = input().split()
    st.append((-int(t), s))
st.sort()
print(st[1][1])