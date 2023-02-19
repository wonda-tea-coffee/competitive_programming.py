def comparison(a, b):
    lena = len(a)
    lenb = len(b)
    if lena > lenb:
        return "GREATER"
    elif lena < lenb:
        return "LESS"

    for i in range(lena):
        if a[i] > b[i]:
            return "GREATER"
        elif a[i] < b[i]:
            return "LESS"

    return "EQUAL"

A = input()
B = input()
print(comparison(A, B))
