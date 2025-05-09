N = int(input())
prev_t, prev_x, prev_y = 0, 0, 0

for n in range(N):
    t, x, y = map(int, input().split())

    distance = abs(prev_x - x) + abs(prev_y - y)
    time = t - prev_t

    if distance > time or (time - distance) % 2 != 0:
        print("No")
        exit()    
    
    prev_t, prev_x, prev_y = t, x, y

print("Yes")
