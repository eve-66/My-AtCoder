from collections import deque

N, M = map(int, input().split())
edges = list([] for _ in range(N))
nodes = [False] * N
for _ in range(M):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)

Q = int(input())
visited = [0] * N
bfs_id = 0
for _ in range(Q):
    query_1, query_2 = map(int, input().split())
    if query_1 == 1:
        nodes[query_2 - 1] = True
    else:
        bfs_id += 1
        start = query_2 - 1
        node_queue = deque([start])
        flag = False
        visited[start] = bfs_id

        while node_queue and not flag:
            node = node_queue.popleft()
            if nodes[node]:
                print("Yes")
                flag = True
                break
            for to in edges[node]:
                if  visited[to] == bfs_id:
                    continue
                visited[to] = bfs_id
                if nodes[to]:
                    print("Yes")
                    flag = True
                    break
                node_queue.append(to)
        if not flag:
            print("No")

