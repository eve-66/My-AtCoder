N = int(input())

answer = 0
for n in range(1, N+1):
  if len(str(n)) % 2 == 1:
    answer += 1
print(answer)