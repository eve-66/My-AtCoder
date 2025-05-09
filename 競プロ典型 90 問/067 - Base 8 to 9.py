def convert(N):
    n = int(N, 8) #Nの10進数表記
    Nonary = [] #8進数表記格納リスト

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
