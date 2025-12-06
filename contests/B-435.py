N = int(input())
A = list(map(int, input().split()))

count = 0
for l in range(N-1):
    for r in range(l+1, N):
        sum_A = sum(A[l:r+1])
        flag = True
        for i in range(l, r+1):
            if sum_A % A[i] == 0:
                flag = False
                break
        if flag:
            count += 1

print(count)
    
