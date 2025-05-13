def convert(N):
    n = int(N, 8) #Nの10進数表記
    Nonary = [] #9進数表記格納リスト

    while n>=9:
        Nonary.insert(0, n%9) #9で割った余りをリストの先頭に格納
        n = n//9

    if not n == 0:
        Nonary.insert(0, n)

    Octal_numeral = [5 if i == 8 else i for i in Nonary]
    Octal_numeral=[str(a) for a in Octal_numeral]
    answer = "".join(Octal_numeral)
    return answer

N, K = map(str, input().split())
for _ in range(int(K)):
    if N == '0': #例外処理
        break
    N = convert(N)

print(N)

# N, K = map(int, input().split())

# def eight_to_ten(n):
#   n = str(n)
#   i = 0
#   ten_base = 0
#   for num in reversed(n):
#     ten_base += int(num) * (8 ** i)
#     i += 1
#   return ten_base

# def ten_to_nine(n):
#   nine_base = ''
#   while n >= 9:
#     nine_base = str(n % 9) + nine_base
#     n //= 9
#   nine_base = str(n) + nine_base
#   return nine_base

# answer = N
# for _ in range(K):
#   ten_base = eight_to_ten(answer)
#   nine_base = ten_to_nine(ten_base)
#   answer = int(nine_base.replace('8', '5'))

# print(answer)

