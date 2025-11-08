N, M = map(int, input().split())
S = [list(line) for line in [input() for _ in range(N)]]
grid = []

for x_index in range(0, N-M+1):
    for y_index in range(0, N-M+1):
        subgrid = [row[y_index:y_index+M] for row in S[x_index:x_index+M]]
        grid.append(subgrid)

# リストをタプルに変換してユニークな数を調べる
unique_grids = set(tuple(tuple(row) for row in subgrid) for subgrid in grid)
print(len(unique_grids))
