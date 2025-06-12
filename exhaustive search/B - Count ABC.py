N = int(input())
S = input()

answer = 0
for i in range(N-2):
  if S[i] == 'A'and S[i+1] == 'B' and S[i+2] == 'C':
    answer += 1

print(answer)