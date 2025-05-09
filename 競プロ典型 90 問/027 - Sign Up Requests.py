N = int(input())
Names = set() #リストの要素の検索はO(n), setは要素の検索がO(1)

for n in range(N):
    name = input()
    if not(name in Names):
        Names.add(name)
        print(n+1)
    else:
        continue