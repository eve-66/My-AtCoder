X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

check = [False] * N
weight = X
for _ in range(Q):
  P = int(input())
  if check[P-1] == False:
    weight += W[P-1]
    check[P-1] = True
  else:
    weight -= W[P-1]
    check[P-1] = False
  print(weight)
