Q = int(input())

deck = []

for _ in range(Q):
    t, x = map(int, input().split())
    
    if t == 1:
        deck.insert(0, x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])

# from collections import deque

# Q = int(input())

# deck = deque()
# for _ in range(Q):
#   t, x = map(int, input().split())
#   if t == 1:
#     deck.appendleft(x)
#   elif t == 2:
#     deck.append(x)
#   else:
#     print(deck[x-1])

