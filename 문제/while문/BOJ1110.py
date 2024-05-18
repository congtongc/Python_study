# 더하기 사이클
import sys;input=sys.stdin.readline
N = int(input())
tmp = 0
num = N

while True:
    num1 = num//10
    num2 = num%10
    num3 = (num1+num2)%10
    num = (num2*10)+num3
    tmp += 1
    if num == N:
        print(tmp)
        break