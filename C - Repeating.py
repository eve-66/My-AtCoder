N = int(input())
A = list(map(int, input().split()))
l = [-1]*(10**9)
ans = []

for i in range(N):
    ans.append(l[A[i]-1])
    l[A[i]-1] = i+1

print(ans)