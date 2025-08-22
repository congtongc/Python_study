import sys; input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*5 for _ in range(5)]

def dfs(x,y,apple_count):
    visited[x][y] = True
    if apple_count >= 2:
        return True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and board[nx][ny] != -1:
            if board[nx][ny] == 1:
                apple_count += 1
            if dfs(nx, ny, apple_count):
                return True
            if board[nx][ny] == 1:
                apple_count -= 1
    visited[x][y] = False
    return False

board = [list(map(int, input().split())) for _ in range(5)]
r,c = map(int, input().split())

if dfs(r, c, 0):
    print(1)
else:
    print(0)