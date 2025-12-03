X = list(map(int, input()))
X.sort()

i = 0
while X[i] == 0:
    i += 1

while i > 0:
    temp = X[i]
    X[i] = X[i-1]
    X[i-1] = temp
    i -= 1

ans = [str(a) for a in X]
ans = "".join(ans)
print(ans)
