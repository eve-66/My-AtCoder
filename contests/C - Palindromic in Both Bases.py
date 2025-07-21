def is_palindrome(x: int, base: int) -> bool: #n進数での回文チェック
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    return digits == digits[::-1]


A = int(input())
N = int(input())

max_len = len(str(N))
ans = 0

for length in range(1, max_len + 1): #各桁数時の回文数のみ抽出する
    half_len = (length + 1) // 2 #1以上
    start = 10 ** (half_len - 1) #0乗以上
    end = 10 ** half_len #1乗以上

    for n in range(start, end): #各桁数の回文を作成
        n_str = str(n)
        if length % 2 == 0: #偶数桁数
            pal_str = n_str + n_str[::-1]
        else: #奇数桁数
            pal_str = n_str + n_str[:-1][::-1] #末尾を一つ除去してから反転
        pal = int(pal_str)
        if pal > N:
            break
        if is_palindrome(pal, A):
            ans += pal

print(ans)