H, W, N = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

ans = [0] * H

for _ in range(N):
    b = input()
    for i in range(H):
        if b in A[i]:
            ans[i] += 1
            break

print(max(ans))
