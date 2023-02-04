S = input()
ans = False
for i in range(10):
    if S.count(str(i) + str(i)):
        ans = True
        break
if ans:
    print("Bad")
else:
    print("Good")