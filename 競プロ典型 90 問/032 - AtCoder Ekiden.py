import itertools

N = int(input())
A = [list(map(int, input().split())) for l in range(N)]
M = int(input())
B = [[0 for _ in range(N)] for _ in range(N)] #N行N列の配列を用意

for _ in range(M):
    x, y = map(int, input().split())
    B[x-1][y-1] = B[y-1][x-1] = 1 #仲の悪い関係の要素を1に変換

ans = 10**9
for p in list(itertools.permutations(range(N))): #1~10の順列
    tmp = 0
    for i in range(len(p)):
        tmp += A[p[i]][i] #p[i]の番号の人がi区間を走る時間を加算
        if i < len(p)-1 and B[p[i]][p[i+1]] == 1: #最後の人以外は,次の区間の人との相性を確認
            break
    else:
        if tmp < ans:
            ans = tmp
print(ans if ans != 10 ** 9 else -1)