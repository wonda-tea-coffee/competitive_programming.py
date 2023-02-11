N, LIM, CHARGE, STOP = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# タスクの最初に戻る直前の状態
history = set()
ans = 0
ti = 0
# 負荷の上限以上のタスクが続いた秒数
s = 0
while ti < N:
    # print("task:", ti+1, "/ ans:", ans)
    if B[ti] < LIM:
        s = 0
        ans += A[ti]
        ti += 1
    else:
        if s + A[ti] < CHARGE:
            s += A[ti]
            ans += A[ti]
            ti += 1
        elif s + A[ti] == CHARGE:
            # print("  STOP1")
            s = 0
            ans += A[ti]
            ans += STOP
            ti += 1
        else: # s + A[ti] > CHARGE
            # print("  STOP2", CHARGE - s)
            # s + x = CHARGE <=> x = CHARGE - s
            if (ti, CHARGE - s) in history:
                print("forever")
                exit()
            else:
                history.add((ti, CHARGE - s))

            # tiは増減無し
            ans += CHARGE - s + STOP
            s = 0

# print(ans, history)
print(ans)
