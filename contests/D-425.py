H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_grid(x, y):
    return 0 <= x < H and 0 <= y < W

def count(x, y):
    count = 0
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny) and S[nx][ny] == '#':
            count += 1
    return count

for i in range(H * W):
    if i == 0:
        T = []
        for h in range(H):
            for w in range(W):
                if S[h][w] == '.' and count(h, w) == 1:
                    T.append((h, w))
    else:
        nT = []
        for h, w in T:
            for dx, dy in dxdy:
                nh, nw = h + dx, w + dy
                if in_grid(nh, nw) and count(nh, nw) == 1 and S[nh][nw] == '.':
                    nT.append((nh, nw))
        T = nT
    if len(T) == 0:
        break
    for x, y in T:
        S[x][y] = '#'

ans = 0
for x in range(H):
    for y in range(W):
        if S[x][y] == '#':
            ans += 1
print(ans)
