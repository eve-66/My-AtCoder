from collections import deque

N ,Q = map(int, input().split())
A = deque(list(map(int, input().split())))

tmp = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        tmp = A[x-1]
        A[x-1] = A[y-1]
        A[y-1] = tmp
    elif T == 2:
        A.rotate(1)
    else:
        print(A[x-1])
