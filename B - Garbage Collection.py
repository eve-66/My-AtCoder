N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
Q = int(input())

for _ in range(Q):
    t, d = map(int, input().split())
    q = l[t-1][0]
    r = l[t-1][1]
    amari = d % q
    if amari < r :
        ans = d + (r - amari)
    elif amari > r:
        ans = d + (q - amari) + r
    else: 
        ans = d
    print(ans)


        

