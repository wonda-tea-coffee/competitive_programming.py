def levenshteinDistance(s, t):
    lent = len(t)
    cur = list(range(lent+1))
    for i in range(1, len(s)+1):
        prev = cur
        cur = [i]*(lent+1)
        for j in range(1, lent+1):
            cost = 0 if s[i-1] == t[j-1] else 1
            cur[j] = min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + cost)

    return cur[-1]

S = input()
T = input()
print(levenshteinDistance(S, T))
