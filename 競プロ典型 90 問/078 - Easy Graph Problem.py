# N, M = map(int, input().split())
# vertex = [0]*N

# for _ in range(M):
#     a, b = map(int, input().split())
#     if a > b:
#         vertex[a-1] += 1
#     elif a < b:
#         vertex[b-1] += 1

# print(vertex.count(1))

N, M = map(int, input().split())
vertex = [[] for _ in range(N)] 

for _ in range(M):
  a, b = map(int, input().split())
  vertex[a-1].append(b)
  vertex[b-1].append(a)
  # print(vertex)

count = 0
for n in range(N):
  # print(vertex[n])
  small = sum(x < n+1 for x in vertex[n])
  if small == 1:
    count += 1

print(count)