def unbalance(N, lst):
    X = 0
    for _ in range(N):
        X = max(X, max(lst) - min(lst))
        lst = [lst[i] + lst[i+1] for i in range(0, len(lst), 2)]
    return X

def build(n, k): #再起的に分割して木を構築
    if n == 0:
        return [k]
    a = k // 2
    b = k - a
    return build(n-1, a) + build(n-1, b)

N, K = map(int, input().split())

ans_list = build(N, K)

X = unbalance(N, ans_list)

print(X)
print(*ans_list)
