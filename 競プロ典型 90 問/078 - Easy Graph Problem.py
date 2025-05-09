N, M = map(int, input().split())
vertex = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        vertex[a-1] += 1
    elif a < b:
        vertex[b-1] += 1

print(vertex.count(1))
