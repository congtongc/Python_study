# T = int(input())

# for i in range(T):
#     stack = []
#     VPS = input()
#     for j in VPS:
#         if j == '(':
#             stack.append(j)
#         elif j == ')':
#             if len(stack) == 0:
#                 print('NO')
#                 break
#             else:
#                 stack.pop()
#         else:
#             if len(stack) == 0:
#                 print('YES')
#             else:
#                 print('NO')

import sys

T = int(sys.stdin.readline())
for i in range(T):
    stack = 0
    VPS = sys.stdin.readline()
    for i in VPS:
        if i == '(':
            stack += 1
        elif i == ')':
            if stack == 0:
                print('NO')
                break
            else:
                stack -= 1
        else:
            if stack == 0:
                print('YES')
            else:
                print('NO')