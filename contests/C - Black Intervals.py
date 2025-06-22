N, Q  = map(int, input().split())
queries = list(map(int, input().split()))

A = [0] * N

answer = 0

for a in queries:
  a -= 1
  was_block = A[a]

  left_block = (a > 0 and A[a - 1] == 1)
  right_block = (a < N - 1 and A[a + 1] == 1)

  if was_block:
    if left_block and right_block:
      answer += 1
    elif not left_block and not right_block:
      answer -= 1
  else:
    if left_block and right_block:
      answer -= 1
    elif not left_block and not right_block:
      answer += 1
  A[a] = 1 - A[a]
  print(answer)