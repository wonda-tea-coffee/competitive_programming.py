# 長さが偶数の回文の中央は必ず同じ文字が揃う(ex. aa)
# 長さが奇数の回文の中央は必ずabaのようになる
# つまり上記2パターンさえ回避できればいい

S = input()
A = sorted([S.count("a"), S.count("b"), S.count("c")])

if A[2]-A[0] <= 1:
    print("YES")
else:
    print("NO")
