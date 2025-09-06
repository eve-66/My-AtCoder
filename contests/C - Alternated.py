N = int(input())
S = input()

X = [i+1 for i , c in enumerate(S) if c =='A']

Y1 = [2*k - 1 for k in range(1, N+1)]
Y2 = [2*k for k in range(1, N+1)]

ops1 = sum(abs(x-y) for x, y in zip(X, Y1))
ops2 = sum(abs(x-y) for x, y in zip(X, Y2))

print(min(ops1, ops2))