# 나머지
a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)
print(int((A+B)%C))
print(int(((A%C)+(B%C))%C))
print(int((A*B)%C))
print(int(((A%C)*(B%C))%C))