# 一周の長さ: M
# 古屋: 1
# 立っている人: N
# 出会った人の合計基準: C
N, M, C = map(int, input().split())
# i番目の人のポジション
A = list(map(int, input().split()))

if C == 0:
    print(0)
    exit()

A.sort()
B = []
P = []
i = 0
while i < N:
    pos = A[i]
    j = i + 1
    while j < N and A[j] == pos:
        j += 1
    B.append(pos)
    P.append(j - i)
    i = j

K = len(B)
ans = 0
r = 0
cur = 0

for i in range(K):
    while cur < C:
        cur += P[r]
        r += 1
        if r >= K:
            r-= K
    if i == 0:
        seg_len = M + B[0] - B[K - 1]
    else:
        seg_len = B[i] - B[i - 1]
    ans += seg_len * cur
    cur -= P[i]

print(ans)
