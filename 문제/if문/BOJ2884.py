# 알람시계
H,M = list(map(int,input().split()))
if H>0:
    if M-45>=0:
        print('%d %d' %(H,M-45))
    else:
        print('%d %d' %(H-1,60+(M-45)))
elif H==0:
    if M-45>=0:
        print('%d %d' %(H,M-45))
    else:
        print('%d %d' %(24+(H-1),60+(M-45)))
else:
    if M-45>=0:
        print('%d %d' %(24+(H-1),M-45))
    else:
        print('%d %d' %(24+(H-1),60+(M-45)))