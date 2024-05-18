# A+B - 8
import sys;input=sys.stdin.readline
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print('Case #%d: %d + %d = %d' %(i+1,A,B,A+B))