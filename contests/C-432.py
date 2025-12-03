N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A1 = A[0]

den = Y - X
D = [0] * N

for k in range(1, N):
  diff = A[k] - A1
  num = diff * X

  if num % den != 0:
      print(-1)
      exit()

  d = num // den

  if d > A1:
      print(-1)
      exit()

  D[k] = d

x1 = A1
ans = 0
for k in range(N):
   ans += x1 - D[k]

print(ans)
