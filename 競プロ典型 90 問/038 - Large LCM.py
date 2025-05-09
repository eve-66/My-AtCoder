import math
A, B = map(int, input().split())

ans = math.lcm(A,B)
if ans > 10**18:
    print('Large')
else:
    print(ans)