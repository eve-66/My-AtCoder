N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [int(input()) for _ in range(Q)]

maxA = max(A)
maxB = max(B)
L = max(maxA, maxB) + 2

C = [0] * L
S = [0] * L
for a in A:
    C[a] += 1
    S[a] += a
for i in range(1, L):
    C[i] += C[i - 1]
    S[i] += S[i - 1]

for b in B:
    ans = S[b-1]
    ans += (N - C[b-1]) * (b-1)
    ans += 1
    if b > maxA:
        ans = -1
    print(ans)
