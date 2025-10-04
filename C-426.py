N, Q = map(int, input().split())
min_ver = 0
versions = [i for i in range(1, int(N)+1)]

for _ in range(Q):
    X, Y = map(int, input().split())
    if X <= min_ver:
        print(0)
        continue
    print(versions[X-1])
    versions[Y-1] += versions[X-1]
    min_ver = X
