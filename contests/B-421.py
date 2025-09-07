X, Y = map(int, input().split())

def a (x, y):
    total = x + y
    total_r = str(total)[::-1]
    return int(total_r)

answer = 0
for _ in range(8):
    answer = a(X, Y)
    X, Y = Y, answer

print(answer)