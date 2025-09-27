N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
point = [0] * N
for idx, a in enumerate(A):
    if a != -1:
        if point[a-1] >= 1:
            print("No")
            exit()
        ans[idx] = a
        point[a-1] += 1

for i in range(N):
    if ans[i] == 0:
        ans[i] = point.index(0) + 1
        point[point.index(0)] += 1
print("Yes")
print(*ans)
