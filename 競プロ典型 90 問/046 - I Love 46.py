import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a = []
b = []
c = []
for i in range(N): #modを考える
    a.append(A[i] % 46)
    b.append(B[i] % 46)
    c.append(C[i] % 46)

#あまりの各数を計算
count_a = collections.Counter(a)
count_b = collections.Counter(b)
count_c = collections.Counter(c)

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += count_a[i]*count_b[j]*count_c[k]

print(ans)


