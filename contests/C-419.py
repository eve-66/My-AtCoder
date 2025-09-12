N = int(input())
min_r = float('inf')
max_r = float('-inf')
min_c = float('inf')
max_c = float('-inf')
for _ in range(N):
    r, c = map(int, input().split())
    if r < min_r:
        min_r = r
    if r > max_r:
        max_r = r
    if c < min_c:
        min_c = c
    if c > max_c:
        max_c = c

ans = max((max_r - min_r + 1)//2, (max_c - min_c + 1)//2)
print(ans)