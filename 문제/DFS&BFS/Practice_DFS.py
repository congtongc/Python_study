V = 0
adj = []

def Graph(v):
    global V, adj
    V = v
    adj = [[] for _ in range(v)]
    
def addEdge(v,w):
    adj[v].extend([w])
    
def DFS(v):
    visited = [False]*(V+1)
    stack = [v]
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            print(curr, end=' ')
            for i in adj[curr]:
                if not visited[i]:
                    stack.append(i)
            
def main():
    Graph(5)
    addEdge(0,1)
    addEdge(0,2)
    addEdge(1,2)
    addEdge(2,0)
    addEdge(2,3)
    addEdge(3,3)
    DFS(2)    
    
main()