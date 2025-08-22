from collections import deque

V = 0
adj = []

def Graph(v):    
    global V, adj
    V = v
    adj = [[] for _ in range(V)]

def addEdge(v, w):
    adj[v].extend(w)
    
def BFS(s):
    visited = [False] * (V+1)
    q = deque()
    visited[s] = True
    q.append(s)
    while q:
        s = q.popleft()
        print(s, end=' ')
        for i in adj[s]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                
def main():
    Graph(5)
    addEdge(0, [1, 2])
    addEdge(1, [0, 2])
    addEdge(2, [0, 1, 3])
    addEdge(3, [2, 4])
    addEdge(4, [3])
    BFS(2)
    
main()