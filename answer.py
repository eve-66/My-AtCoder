N = int(input())

plans = []

for _ in range(N):
  t, x, y = map(int, input().split())
  plans.append((t, x, y))

prev_time, prev_x, prev_y = 0, 0, 0

is_possible = True

for t, x, y in plans:
  distance = abs(x - prev_x) + abs(y - prev_y)
  time_difference = t - prev_time

  if distance > time_difference or (time_difference - distance) % 2 != 0:
    is_possible = False
    break

  prev_time, prev_x, prev_y = t, x, y

if is_possible:
  print('Yes')
else:
  print('No')