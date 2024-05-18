x = int(input('가로의 값을 입력하세요 : '))
y = int(input('세로의 값을 입력하세요 : '))
for i in range(0,x,1):
        print("* " * y)

x = int(input('숫자를 입력하세요 : '))
for i in range(1,x+1,1):
    print(" " * (x-i) + "* " * i)

x = int(input('숫자를 입력하시오 : '))
for i in range(1,x+1):
    if (i%5 != 0):
        print(i , end = ' ')
print()

