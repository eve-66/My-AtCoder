N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
  Check = [0] * (M+1)
  for j in range(len(A)):
    if A[j] <= M:
      Check[A[j]] = 1

  if(sum(Check) < M):
    print(i)
    exit()
  else:
    A.pop(-1)

print(N)

