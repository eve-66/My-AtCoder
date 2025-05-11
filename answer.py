N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

difference = 0
for n in range(N):
  difference += abs(A[n] - B[n])

if K >= difference and (K - difference) % 2 == 0:
  print('Yes')
else:
  print('No')


