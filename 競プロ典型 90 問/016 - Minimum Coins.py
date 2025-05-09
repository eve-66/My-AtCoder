import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
A, B, C = map(int, input().split())
Num = 9999

for i in range(10000): #AとBの硬貨の組み合わせを考える
    for j in range(10000-i):
        Balance = N - A*i - B*j #残金をCで綺麗に払いきれるかを判定する
        if Balance < 0:
            break
        if Balance % C == 0 :
            k = Balance // C
            Num = min(Num, i+j+k)

print(Num)
