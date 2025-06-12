S = input()

answer_len = 0
current_len = 0

for s in S:
  if s in 'ACGT':
    current_len += 1
    answer_len = max(answer_len, current_len)
  else:
    current_len = 0

print(answer_len)