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