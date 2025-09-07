N, M = map(int, input().split())
S = [ input() for _ in range(N)]

P = [0] * N

for i in range(M):
    zero = 0
    one = 0
    for j in range(N):
        if S[j][i] == '0':
            zero += 1
        else:
            one += 1
    if zero == 0 or one == 0:
        P = [p + 1 for p in P]
    elif zero > one:
        for j in range(N):
            if S[j][i] == '0':
                P[j] += 1
    else:
        for j in range(N):
            if S[j][i] == '1':
                P[j] += 1
print(P)