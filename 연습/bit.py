x = int(input('숫자를 입력하세요 : '))
a = 2
for i in range(0, x+1):
    print('{0:6,}'.format(a ** i), end = ' ')
print()

x = int(input('숫자를 입력하세요 : '))
a = 1
for i in range(0, x+1):
    print('{0:6,}'.format(a<<i), end = ' ')
print( )