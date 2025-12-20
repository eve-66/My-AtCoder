T = int(input())

for _ in range(T):
    N = int(input())
    reins = [0] * N
    sum_P = 0
    for i in range(N):
        W, P = map(int, input().split())
        sum_P += P
        reins[i] = P + W
    reins.sort()

    ans = 0
    i = 0
    while i < N and sum_P >= reins[i]:
        sum_P -= reins[i]
        ans += 1
        i += 1

    print(ans)
