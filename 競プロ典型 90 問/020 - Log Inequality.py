import math
a, b, c = map(int,input().split())

left = a
right = c ** b #PCは2進数で計算するためlogやrootの計算は誤差が発生する

if left < right:
    print('Yes')
else:
    print('No')