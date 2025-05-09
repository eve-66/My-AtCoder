from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = int(input())

for _ in range(Q):
    B = int(input())

    left = -1
    right = N

    while right-left>1: #クイックソート
        pivot = (right + left)//2
        if A[pivot] <= B:
            left = pivot
        else:
            right = pivot

    abs1 = 10**9 #前回の計算を残さないようにリセット
    abs2 = 10**9
    if left >= 0:
        abs1 = abs(A[left]-B)
    if left < N-1:
        abs2 = abs(A[left+1]-B)
    print(min(abs1, abs2))

