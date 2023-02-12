N = int(input())
s = input()
rc = s.count("R")
if rc > N - rc:
    print("Yes")
else:
    print("No")