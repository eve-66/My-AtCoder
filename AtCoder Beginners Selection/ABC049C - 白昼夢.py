S = input().strip()[::-1]

words = ["dream", "dreamer", "erase", "eraser"]
words = [word[::-1] for word in words]

while len(S) > 0:
    matched = False
    for word in words:
        if S.startswith(word):
            S = S[len(word):]
            matched = True
            break
    if not matched:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")