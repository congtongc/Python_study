import sys; input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break               # 세 숫자가 0이면 합도 0

    max_num = max(nums)     # 셋 중 가장 큰 숫자 등록
    nums.remove(max_num)    # 가장 큰 숫자 nums리스트에서 제거

    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
        
    else:
        print('wrong')

# count = 0

# while True:
#     a,b,c = sorted(map(int,input().split()))
#     count += count
#     if a == 0 and b == 0 and c ==0:
#         break

# for i in range(count-2):
#     if a[i]**2 == b[i]**2 + c[i]**2:
#         print('right')
#     elif b[i]**2 == a[i]**2 + c[i]**2:
#         print('right')
#     elif c[i]**2 == a[i]**2 + b[i]**2:
#         print('right')
#     else:
#         print('wrong')