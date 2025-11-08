
H, B = map(int, input().split())

ans = 0
if H <= B:
  ans = 0
else:
  ans = H - B
print(ans)
