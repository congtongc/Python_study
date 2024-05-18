# 평균은 넘겠지
C = int(input())

for i in range(C):
    S = list(map(int,input().split()))
    average = sum(S[1:])/S[0]
    stp = 0

    for i in S[1:]:

        if i > average:
            stp += 1

    result = (stp / S[0]) * 100 

    print('{:0.3f}%'.format(round(result,3)))  