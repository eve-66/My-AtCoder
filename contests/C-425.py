N, Q = map(int, input().split())
A = list(map(int, input().split()))
A += A
acc_A = [0] * (2 * N + 1)
for idx, a in enumerate(A):
    acc_A[idx+1] = acc_A[idx] + a

head = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        head += query[1]
        head %= N

    elif query[0] == 2:
        l, r = query[1], query[2]
        start = head + l - 1
        end = head + r
        print(acc_A[end] - acc_A[start])
