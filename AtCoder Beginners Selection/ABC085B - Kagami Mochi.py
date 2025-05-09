N = int(input())
D = []
for x in range(N):
    d = int(input())
    if not(d in D):
        D.append(d)

# D = [ int(input()) for _ in range(N)]
# len(set(D))

print(len(D))
