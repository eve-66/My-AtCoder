N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

count = 0
for h in reversed(H):
  b = B[-1]
  if h <= b:
    count += 1
    B.pop()
    if len(B) == 0:
      break
if count >= K:
  print("Yes")
else:
  print("No")
