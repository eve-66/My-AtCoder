ans = 0

for i in range(12):
    S = input()
    if len(S) == i+1:
        ans += 1

print(ans)