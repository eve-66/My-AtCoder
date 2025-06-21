N, Q  = map(int, input().split())

A = list(map(int, input().split()))

list = []
len = 0

for a in A:
  left = 0
  right = len

  while left < right:
    center = (left + right) // 2
    if(list[center] < a):
      left = center + 1
    else:
      right = center

  if(left < len and list[left] == a):
    list.pop(left)
    len -= 1
  else:
    list.insert(left, a)
    len += 1

  if len == 1:
    print(1)
    continue
  elif len == 0:
    print(0)
    continue
  else:
    answer = 1
    start = 0
    end = 1
    while end < len:
      if list[end] - list[start] <= 1:
        start += 1
        end += 1
      else:
        answer += 1
        start = end
        end += 1

    print(answer)

