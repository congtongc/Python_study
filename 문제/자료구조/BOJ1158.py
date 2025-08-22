N,K = map(int,input().split())
list = [i for i in range(1,N+1)]
result = []
index = 0

while list:
    index = (index+K-1) % len(list)
    result.append(list.pop(index))
    
print("<" + ", ". join(map(str,result)) + ">")