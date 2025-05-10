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


# N = int(input())
# A = list(map(int, input().split()))
# Q = int(input())
# A.sort()

# for _ in range(Q):
#   left = 0
#   right = N - 1
#   B = int(input())

#   while(right - left > 1):
#     mid = int((left + right) / 2)

#     if(B <= A[mid]):
#       right = mid
#     else:
#       left = mid

#   l = abs(A[left] - B)
#   r = abs(A[right] -B)

#   if(l<r):
#     Dissatisfaction = l
#   else:
#     Dissatisfaction = r

#   print(Dissatisfaction)

