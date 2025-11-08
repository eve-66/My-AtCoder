N = int(input())
parts = list(list(map(int, input().split())) for _ in range(N))

head = 0
body = 0
happy = 0
for part in parts:
    body += part[0]
    happy += part[2]

parts.sort(key=lambda x: x[0])

for part in parts:
  if body - part[0] == 0:
     break
  elif body - part[0] >= head:
    if part[1] > part[2]:
      body -= part[0]
      head += part[0]
      happy += part[1] - part[2]
  else:
     break
print(happy)
