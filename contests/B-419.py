Q = int(input())
balls = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        balls.append(query[1])
    elif query[0] == 2:
        print(min(balls))
        balls.remove(min(balls))