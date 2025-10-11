X, Y = input().split()

if Y == 'Ocelot':
    print('Yes')
    exit()
elif Y == 'Serval':
    if X == 'Serval' or X == 'Lynx':
        print('Yes')
        exit()
elif Y == 'Lynx':
    if X == 'Lynx':
        print('Yes')
        exit()

print('No')
