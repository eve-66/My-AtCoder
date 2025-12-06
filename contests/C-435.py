N = int(input())
A = list(map(int, input().split()))

B = [0] * N
for idx, a in enumerate(A):
    B[idx] = idx + (a -1)

i = 0
max = B[0]
while i < N and i <= max:
    if B[i] > max:
        max = B[i]
    i += 1

print(i)
