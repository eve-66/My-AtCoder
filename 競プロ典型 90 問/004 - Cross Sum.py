H, W = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(H)]
B = []

#各行の和を事前計算
L = []
for h in range(H):
    L.append(sum(A[h]))

#各列の和を事前計算
R = []
for w in range(W):
    total = 0
    for h in range(H):
        total += A[h][w]
    R.append(total)

#行列Bを計算
for h in range(H):
    total = 0
    l = []
    for w in range(W):
        total = L[h] + R[w] - A[h][w]
        l.append(total)
    B.append(l)


#行列Bを出力
for h in range(H):
    print(*B[h])

    H, W = map(int, input().split())

# X = [list (map(int, input().split())) for _ in range(H)]
# line = [sum(X[i]) for i in range(H)]
# column = [sum(X[j][i] for j in range(H)) for i in range(W)]
# Y = [[line[i] + column[j] - X[i][j] for j in range(W)] for i in range(H)]

# for i in range(H):
#   print(*Y[i])
