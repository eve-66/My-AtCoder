A = list(map(int, input().split()))

count1 = A.count(1)
count2 = A.count(2)
count3 = A.count(3)
count4 = A.count(4)

ans = 0
ans += int(count1 / 2)
ans += int(count2 / 2)
ans += int(count3 / 2)
ans += int(count4 / 2)

print(ans)




