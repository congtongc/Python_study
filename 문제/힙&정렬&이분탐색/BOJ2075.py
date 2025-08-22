# 힙 사용
import heapq

N = int(input())
nums = []

for _ in range(N):
    row = list(map(int, input().split()))
    if not nums:    
        for num in row:
            heapq.heappush(nums, num)
    else:
        for num in row:
            if num > nums[0]:
                heapq.heappushpop(nums, num)
                    
print(nums[0])

# # 정렬 사용(메모리 초과)
# N = int(input())
# nums = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     nums.extend(row)
# nums.sort(reverse=True)
# nth_largest = nums[N-1]
# print(nth_largest)