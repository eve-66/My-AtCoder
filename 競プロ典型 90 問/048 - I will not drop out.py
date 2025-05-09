N, K = map(int, input().split())
point = []

for _ in range(N):
    A, B = map(int, input().split())
    sub = A-B
    point.append(B)
    point.append(sub)
    
point.sort(reverse = True)
ans = sum(point[:K])
print(ans)

    
