#生徒数を取得
N = int(input())
Class_1 = [0]*N
Class_2 = [0]*N

#入力データを取得
for num in range(N):
    C, P = map(int, input().split())
    if C == 1:
        Class_1[num] = P
    else:
        Class_2[num] = P

#累積和のリストを作成
ComulativeSum_1 = [0]*(N+1)
ComulativeSum_2 = [0]*(N+1)

for num in range(N):
    ComulativeSum_1[num+1] = ComulativeSum_1[num] + Class_1[num]
    ComulativeSum_2[num+1] = ComulativeSum_2[num] + Class_2[num]

#質問数を取得
Q = int(input())

#質問に解答
for _ in range(Q):
    L, R = map(int, input().split())
    
    answer_1 = ComulativeSum_1[R] - ComulativeSum_1[L-1]
    answer_2 = ComulativeSum_2[R] - ComulativeSum_2[L-1]

    print(answer_1, answer_2)

# N = int(input())

# students = []
# total_A = 0
# total_B = 0
# for _ in range(N):
#   C, P = map(int, input().split())
#   if C == 1:
#     total_A += P
#   else:
#     total_B += P
#   students.append([total_A, total_B])

# Q = int(input())
# for _ in range(Q):
#   L, R = map(int, input().split())
#   if(L != 1):
#     score_A = students[R-1][0] - students[L-2][0]
#     score_B = students[R-1][1] - students[L-2][1]
#   else:
#     score_A = students[R-1][0]
#     score_B = students[R-1][1]
#   print(score_A, score_B)

