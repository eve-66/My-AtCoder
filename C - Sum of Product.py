# import itertools

# N = int(input())
# A = list(map(int, input().split()))
# C = list(itertools.combinations(A, 2))

# total = 0
# for i in C:
#   total += i[0]*i[1]
# print(total)

N = int(input())
A = list(map(int, input().split()))

total_sum = sum(A)
squared_sum = sum(x * x for x in A)

result = (total_sum * total_sum - squared_sum) // 2
print(result)