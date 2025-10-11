import itertools

N, M = map(int, input().split())
edge = []
for _ in range(M):
    u, v = map(int, input().split())
    edge.append((u-1, v-1))

min_remove = float('inf')
for coloring in itertools.product([0,1], repeat=N):
    remove = 0
    for u,v in edge:
        if coloring[u] == coloring[v]:
            remove += 1
    if remove < min_remove:
        min_remove = remove

print(min_remove)
