X, Y = map(int, input().split())

answer = (X + Y) % 12

if answer == 0:
    answer = 12

print(answer)