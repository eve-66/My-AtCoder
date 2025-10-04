import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
pc = [0] * (N + 2)  # バージョンごとの台数
for i in range(1, N + 1):
    pc[i] = 1  # 初期状態は1台ずつ

O = 1  # 最古のバージョン

for _ in range(Q):
    X, Y = map(int, input().split())
    cnt = 0
    while O <= X:
        cnt += pc[O]        # アップグレードされる台数
        pc[Y] += pc[O]      # 新しいバージョンに追加
        pc[O] = 0           # 古いバージョンは0に
        O += 1
    print(cnt)
