string = list(input())
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = 0
position = string.index('A')

for i in range(26):
    next = string.index(alphabet[i])
    ans += abs(next - position)
    position = next

print(ans)
    


