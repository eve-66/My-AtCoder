N, M = map(int, input().split())
S = [input() for _ in range(N)]
P = [0] * N

for i in range(M):
  one = 0
  zero = 0
  for j in range(N):
    if S[j][i] == '0':
      zero += 1
    else:
      one += 1
  if zero == 0 or one == 0:
    P = [p + 1 for p in P]
  elif zero > one:
    for j in range(N):
      if S[j][i] == '1':
        P[j] += 1
  elif one > zero:
    for j in range(N):
      if S[j][i] == '0':
        P[j] += 1

max_value = max(P)
max_indices = [i+1 for i, p in enumerate(P) if p == max_value]
print(*max_indices)

# # スマートな書き方
# N, M = map(int, input().split())
# S = [input() for _ in range(N)]

# P = [0] * N
# for i in range(M):
#     col = [S[j][i] for j in range(N)]
#     zeros = col.count('0')
#     ones = col.count('1')
    
#     if zeros == 0 or ones == 0:
#         P = [p + 1 for p in P]
#     elif zeros != ones:
#         minority = '1' if zeros > ones else '0'
#         for j in range(N):
#             if S[j][i] == minority:
#                 P[j] += 1

# max_val = max(P)
# result = [i + 1 for i, p in enumerate(P) if p == max_val]
# print(*result)