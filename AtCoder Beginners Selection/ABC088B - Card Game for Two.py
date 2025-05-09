N =  int(input())
A =  list(map(int, input().split()))
A.sort(reverse = True)
Alice = 0
Bob = 0

for x in range(0, N, 2):
    Alice += A[x]
    if not(x+1>=N):
        Bob += A[x+1]

print(abs(Alice-Bob))