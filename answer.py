T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    mid = N // 2
    point = '0'
    if N % 2 == 1:
        point = S[mid]
        left = S[:mid]
        right = S[mid+1:]
    else:
        if S[mid-1] == S[mid]:
            point = S[mid]
        left = S[:mid-1]
        right = S[mid+1:]
    opposite_point = str(1-int(point))
    if opposite_point in left:
        left_last_idx = len(left) - 1 - left[::-1].index(opposite_point)
        left = left[:left_last_idx+1]
    else:
        left_last_idx = -1
        left = []
    if opposite_point in right:
        right_first_idx = right.index(opposite_point)
        right = right[right_first_idx:]
    else:
        right_first_idx = -1
        right = []
    zero_count = left.count('0') + right.count('0')
    one_count = left.count('1') + right.count('1')
    if point == '0':
        ans = zero_count * 2 + one_count
    else:
        ans = one_count * 2 + zero_count
    print(ans)
