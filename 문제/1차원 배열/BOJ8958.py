# OX퀴즈
N = int(input())

for i in range(N):
    case = input()
    stp = 0
    result = 0
    for i in case:
        if i == 'O':
            stp += 1
        elif i == 'X':
            stp = 0
        result += stp
    print(result) 