import sys
import math
sys.setrecursionlimit(10 ** 6)

a, b, c = map(int, input().split())
gcd = math.gcd(c, math.gcd(a,b))
ans = (a // gcd - 1) + (b // gcd - 1) + (c // gcd - 1)

print(round(ans))