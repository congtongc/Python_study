from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited_D = [False] * (N + 1)
visited_B = [False] * (N + 1)
    
def DFS(n):
    visited_D[n] = True
    print(n, end=' ')
    for i in range(1, N+1):
        if visited_D[i] == False and graph[n][i] == True:
            DFS(i)
                    
def BFS(s):
    q = deque([s])
    visited_B[s] = True
    while q:
        s = q.popleft()
        print(s, end=' ')
        for i in range(1, N+1):
            if not visited_B[i] and graph[s][i]:
                q.append(i)
                visited_B[i] = True

DFS(V)
print()
BFS(V)