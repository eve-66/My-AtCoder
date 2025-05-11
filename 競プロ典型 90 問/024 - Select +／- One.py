import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Sum_A = sum(A)
Sum_B = sum(B)
Sub = abs(Sum_A - Sum_B)

if Sub > K:
    print('No')
elif (K - Sub) % 2 == 1:
    print('No')
else:
    print('Yes')

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# difference = 0
# for n in range(N):
#   difference += abs(A[n] - B[n])

# if K >= difference and (K - difference) % 2 == 0:
#   print('Yes')
# else:
#   print('No')

