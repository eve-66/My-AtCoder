N, A, B = map(int, input().split())
count = 0

for num in range(N+1):
    l = [int(x) for x in list(str(num))]
    if A <= sum(l) <= B:
        count += num

print(count)