A = 30 #int(input())
B = 40 #int(input())
C = 50 #int(input())
X = 6000 #int(input())

count = 0

for a in range(0, A+1):
    for b in range(0, B+1):
        for c in range(0, C+1):
            if 500*a + 100*b + 50*c ==X:
                count += 1

print(count)