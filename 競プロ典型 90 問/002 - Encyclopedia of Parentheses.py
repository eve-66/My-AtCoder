N = int(input())

for  i in range(2**N): #bit全探索
    tmp = ''
    for j in range(N):
        if i & (1<<j): #2進数表記のビット同士を右からand
            tmp = ')' + tmp
        else:
            tmp = '(' + tmp
            
    count = 0 #'('が1で')'が-1と考える
    for i in range(N):
        if tmp[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break   
    if count == 0:
        print(tmp)

