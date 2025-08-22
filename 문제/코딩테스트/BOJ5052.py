import sys;

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    nums = [input().strip() for _ in range(n)]
    nums.sort()
    
    flag = True
    for i in range(n - 1):
        if nums[i + 1].startswith(nums[i]): # 접두사 체크, 해당 문자열 존재 시 flag 값 변경
            flag = False
            break
        
    print("YES" if flag else "NO")