# 곱셈
A = int(input())
B = int(input())
print(A*(B%10))
print(A*((B%100)//10))
print(A*(B//100))
print(A*B)

# A = int(input())
# B = input()
# for i in range(len(B),0,-1):
#     print(A*int(B[i-1]))

# print(A*int(B))