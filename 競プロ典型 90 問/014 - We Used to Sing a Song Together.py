N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

total = 0

for n in range(N):
    total += abs(A[n] - B[n])

print(total)