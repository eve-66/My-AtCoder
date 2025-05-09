import math
N, L = map(int, input().split())
cnt = 0

cnt = N // L + 1
ans = 0

for i in range(cnt):
    L_step = i
    One_step = N - i*L
    total = L_step + One_step
    ans += math.comb(total, L_step) #total _C_ L_step
    

print(ans % (10**9 + 7))