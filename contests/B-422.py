H, W = map(int, input().split())

S = [input() for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            neighbors = []
            if h != 0:
                neighbors.append(S[h-1][w])
            if h != H-1:
                neighbors.append(S[h+1][w])
            if w != 0:
                neighbors.append(S[h][w-1])
            if w != W-1:
                neighbors.append(S[h][w+1])
            black = neighbors.count('#')
            if black == 2 or black == 4:
                continue
            else:
                print("No")
                exit()
print("Yes")
