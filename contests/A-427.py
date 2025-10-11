N = input()

m = (len(N) + 1) / 2 - 1

answer = [N[a] for a in range(len(N)) if a != m]
answer = "".join(answer)
print(answer)
