A, B, K = map(int, input().split())

count = 0
array = []
for i in range(1, min(A, B) + 1):
  if A % i == 0 and B % i == 0:
    array.append(i)

array.sort(reverse = True)
answer = array[K-1]
print(answer)