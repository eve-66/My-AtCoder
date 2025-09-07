N = int(input())
S = [input() for _ in range(N)]

X, Y = map(str, input().split())

if S[int(X)-1] == Y:
  print("Yes")
else:
  print("No")