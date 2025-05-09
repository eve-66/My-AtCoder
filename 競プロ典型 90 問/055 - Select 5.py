from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split())) 

total = 0
combs = combinations(A, 5) #組み合わせを2重リストで整理
for a, b, c, d, e in combs:
    if a % P * b % P * c % P * d % P * e % P == Q:
        total += 1

print(total)

