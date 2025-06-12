N = int(input())

answer = 0
for i in range(1, N+1):
  count = 0
  if i % 2 == 1:
    for j in range(1, i+1):
      if i % j == 0:
        count += 1
    if(count == 8):
      answer += 1

print(answer)