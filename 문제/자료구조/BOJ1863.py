n = int(input())
stack = []
buildings = 0

for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        buildings += 1
    if y != 0:
        stack.append(y)

buildings += len(stack)

print(buildings)