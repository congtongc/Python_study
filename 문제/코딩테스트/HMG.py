from collections import deque
import sys; input = sys.stdin.readline

item = list(map(int, input().split()))
for i in item:
    deque.append(i)



# num = list(map(int,input().split()))
# human = int(input())
# for _ in range(human):
#     benefit = list(map(str,input().split()))
# cnt = 0
# for i in num:
#     if i == 1:
#         if benefit[0] == 'F':
#             cnt += 1
#     elif i == 2:
#         if benefit[1].isalnum() <= 7:
#             cnt += 2