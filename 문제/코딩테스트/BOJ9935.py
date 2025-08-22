import sys

input = sys.stdin.readline

s = input().strip()
bomb = input().strip()

stack = []

for i in s:
    stack.append(i)
    
    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
        
s = ''.join(stack)

# 시간 초과 에러 
# while s.__contains__(bomb):
#     s = s.replace(bomb, '')

print(s if s else "FRULA")