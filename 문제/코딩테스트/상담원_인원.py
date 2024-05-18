import sys; input = sys.stdin.readline

def solution(k, n, reqs):
    answer = 0    
    return answer

while(k < 1 or k > 5):
    k = int(input())
    print(k)
    if(1 <= k and k <= 5):
        break        
    print("입력 값 오류") 
    while(n < k or n > 20):
        n = int(input())
        if(k <= n and n <= 20):
            break
        print("입력 값 오류")            
            
reqs = [list(int(input() for _ in range(3)))]
    
solution(k, n, reqs)