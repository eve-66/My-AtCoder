H, W = map(int, input().split())
datas = []
for h in range(H):
  data = list(input())
  datas.append(data)
print(datas)

passages = []
walls = []
exits = []
for i in range(H):
  for j in range(W):
    if datas[i][j] == '.':
      passages.append([i, j])
    elif datas[i][j] == '#':
      walls.append([i, j])
    else:
      exits.append([i, j])

print (passages)
print(walls)
print(exits)
# passages = [[i, j] ]
# print(passages)

for passage in passages:
  bestexit = [1000, 1000]
  for exit in exits:
    if (abs(sum(bestexit)-sum(passage)) > abs(sum(exit)-sum(passage))):
      bestexit = exit
  print(bestexit)