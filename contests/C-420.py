N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
  answer += min(A[i], B[i])

for _ in range(Q):
  c, x, v = input().split()
  x, v = int(x), int(v)
  gap = 0
  if c == 'A':
    if A[x - 1] < B[x - 1]:
      if B[x - 1] < v:
        gap = B[x - 1] - A[x - 1]
      else:
        gap = v - A[x - 1]
    else:
      if B[x - 1] > v:
        gap = v - B[x - 1]
    A[x - 1] = v
  elif c == 'B':
    if B[x - 1] < A[x - 1]:
      if A[x - 1] < v:
        gap = A[x - 1] - B[x - 1]
      else:
        gap = v - B[x - 1]
    else:
      if A[x - 1] > v:
        gap = v - A[x - 1]
    B[x - 1] = v
  answer += gap
  print(answer)

# スマートな書き方（コメントアウト）
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# answer = sum(min(a, b) for a, b in zip(A, B))

# for _ in range(Q):
#     c, x, v = input().split()
#     x, v = int(x) - 1, int(v)  # 0-indexedに変換
    
#     # 更新前のmin値
#     old_min = min(A[x], B[x])
    
#     # 配列を更新
#     if c == 'A':
#         A[x] = v
#     else:
#         B[x] = v
    
#     # 更新後のmin値
#     new_min = min(A[x], B[x])
    
#     # 差分を計算して更新
#     answer += new_min - old_min
#     print(answer)