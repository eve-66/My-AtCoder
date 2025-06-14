N, Q =  map(int, input().split())

A = [n + 1 for n in range(N)]
for _ in range(Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    A[query[1]-1] = query[2]
  elif query[0] == 2:
    print(A[query[1]-1])
  else:
    A = A + A
    A = A[query[1]: query[1]-N]
