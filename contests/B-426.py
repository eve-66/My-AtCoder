S = input()
count = [0]*26
for s in S:
    count[ord(s) - ord('a')] += 1

print(chr(count.index(1)+ord('a')))
