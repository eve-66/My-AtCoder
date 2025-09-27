N = int(input())

ans = 0
for n in range(N+1):
    ans += ((-1) ** n) * (n ** 3)

print(ans)
