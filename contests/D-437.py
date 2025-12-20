import bisect
import sys

input = sys.stdin.readline
MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + A[i]

total = 0

for b in B:
    # A[i] <= b となる個数
    k = bisect.bisect_right(A, b)

    # 左側
    left = b * k - prefix[k]
    # 右側
    right = (prefix[N] - prefix[k]) - b * (N - k)

    total += left + right
    total %= MOD

print(total)
