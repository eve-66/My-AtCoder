num = 3 #input()
numbers_int = (10, 20, 30) #list(map(int, input().split()))
count = 0

while all( x%2 == 0 for x in numbers_int):
    numbers_int = list(map(lambda x: x/2, numbers_int))
    count += 1
print(count)