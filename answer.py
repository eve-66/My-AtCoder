from collections import Counter

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

R_min = [a*X for a in A]
R_max = [a*Y for a in A]
gap = Y - X
# 前提検査
if min(R_max) < max(R_min):
    print(-1)
    exit()

cnt = Counter(R_max)     # 各値の出現回数
distinct = len(cnt)      # 異なる値の種類数

# 最初だけ A >= 0 を確認
if not all(a >= 0 for a in A):
    print(sum(A))
    exit()

while True:
    if distinct == 1:    # len(set(R_max)) == 1 と同じ
        break
    else:
        big_idx, big_val = max(enumerate(R_max), key=lambda x: x[1])
        old = R_max[big_idx]
        new = old - gap
        R_max[big_idx] = new
        A[big_idx] -= 1
        if A[big_idx] < 0:
            break
        # Counter 更新（old 減少 & new 増加）
        cnt[old] -= 1
        if cnt[old] == 0:
            del cnt[old]
            distinct -= 1

        cnt[new] += 1
        if cnt[new] == 1:
            distinct += 1

ans = sum(A)
print(ans)
