N, M = map(int, input().split())
A = list(map(int, input().split()))


sum_A = sum(A)

for a in A:
    if sum_A - a == M:
        print('Yes')
        exit()
    
print('No')
