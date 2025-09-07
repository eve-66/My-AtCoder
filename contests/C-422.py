T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    num = min (a, c)
    parts = (a-num) + b + (c-num)

    if  num < parts:
        ans = num
    else:
        ans = parts
        ans += (num - parts) * 2 // 3
    
    print(ans)