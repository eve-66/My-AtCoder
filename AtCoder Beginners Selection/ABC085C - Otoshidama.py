N, Y = (int(x) for x in input().split())

for ten_thousand in range(N + 1):
    for five_thousand in range(N - ten_thousand + 1):
        one_thousand = N - ten_thousand - five_thousand
        if ten_thousand*10000 + five_thousand*5000 + one_thousand*1000 == Y:
            print(str(ten_thousand) + ' ' + str(five_thousand) + ' ' + str(one_thousand))
            exit()

print('-1 -1 -1')
