N = int(input())
A = list(map(int, input().split()))

count = [0] * N
for a in A:
    count[a-1] += 1

ans = 0
for c in count:
    if c >= 2:
        conv_2 = c * (c - 1) // 2
        ans += conv_2 * (N - c)

print(ans)
