s1 = 'Computer'
s2 = 'Engineering'
print(s1 +' ' + s2 + '.')
print(s2 * 3)
print('-' * 20)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print(l1 * 3)
print('-' * 30)
print('2 ** 10 = ', 2**10)
print('5/2 = ', 5/2)
print('5//2 = ', 5//2)
print('5 % 2 = ', 5%2)
print('5 + 2.0 = ', 5+2.0)
print('-20 = ', -20)
print('- -20 = ', - -20)
print('산술연산자')
print("-" * 20)

a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print('-' * 20)
print('산술연산자')
print("-" * 20)

a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} // {1} = {2}".format(a, b, a//b))
print("{0} % {1} = {2}".format(a, b, a%b))
print("{0} ** {1} = {2}".format(a, b, a**b))
print('-' * 20)

a = int(input('첫 번째 정수를 입력하세요 : '))
b = float(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} // {1} = {2}".format(a, b, a//b))
print("{0} % {1} = {2}".format(a, b, a%b))
print("{0} ** {1} = {2}".format(a, b, a**b))
print('-' * 20)

print(9/2)
print(9/-2)
print(9//-2)
print(9%-2)
print(-9/2)
print(-9//2)
print(-9%2)

x = 5
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x **= 2
print(x)
x //= 2
print(x)
x %= 2 

birth = int(input('생년월일을 입력하세요 : '))
year = birth // 10000
month1 = birth % 10000 // 100
month2 = birth // 100 % 100
date = birth % 100
print(year, month1, date)
print('생년월일 : {}년 {}월 {}일'.format(year, month2, date))

celsius = int(input('섭씨온도를 입력하세요 : '))
fahrenheit = (9/5) * celsius + 32
print('섭씨', celsius, '도는 화씨', fahrenheit, '도 입니다.')
print('=' * 30)
fahrenheit = float(input('화씨온도를 입력하세요 : '))
celsius = (fahrenheit - 32) * (5/9)
print('화씨', fahrenheit, '도는 섭씨', celsius, '도 입니다.')

print(2020 < 2030)
print(2020 == 2030)
print(2020 != 2030)
print(2020 >= 2030)
print(2020 <= 2030)
print('Security' == 'security')
print('Security' != 'security')
print(2020 == 2020.0)
print(2020 is 2020.0)
print('a' < 'b')
print('ab' < "abc")

no1 = 1
no2 = 1
str1 = 'life'
str2 = 'life'
print(no1 == no2)
print(no1 is no2)
print(str1 == str2)
print(str1 is str2)
print(id(no1))
print(id(no2))
print(id(str1))

no3 = 12345
no4 = 12345
str3 = '죽는 날까지 하늘을 우러러 한 점 부끄러움 없기를...'
str4 = '죽는 날까지 하늘을 우러러 한 점 부끄러움 없기를...'
print(no3 == no4)
print(no3 is no4)
print(str3 == str4)
print(str3 is str4)
print(id(no3))
print(id(no4))
print(id(str3))
print(id(str4))

num = int(input('조건을 확인하고자 하는 수를 입력하세요 : '))
print((num > 2020) and (num < 2030))

year = int(input('연도를 입력하세요 : '))
print(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
print('-' * 40)
print('a = ', a, "=", bin(a))
print('b = ', b, "=", bin(b))
print('a & b = ', a&b, ":", bin(a&b))
print('a | b = ', a|b, ":", bin(a|b))
print('a ^ b = ', a^b, ":", bin(a^b))
print('~a = ', ~a, ":", bin(~a))

a = int(input('숫자를 입력하세요 : '))
print()
print('a = ', a, ":", bin(a))
print('---- < left shift > ----')
a = a << 1  # * 2
print('a << 1 = ', a, ":", bin(a))
a = a << 2  # * 4
print('a << 2 = ', a, ":", bin(a))
a = a << 3  # * 2**3
print('a << 3 = ', a, ":", bin(a))
print()
print('---- < right shift > ----')
a = a >> 1  # / 2
print('a >> 1 = ', a , ":", bin(a))
a = a >> 2  # / 2
print('a >> 2 = ', a , ":", bin(a))
a = a >> 3  # / 2**3
print('a >> 3 = ', a , ":", bin(a))

a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
# 2의 보수를 이용한 뺄셈
c = a - b
d = a + (~b + 1)
print('a - b = ', c)
print('a + (~b + 1) = ', d)

a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
print('-' * 30)
print('두 개의 숫자를 교환하기\n')
print('a = {0}, b = {1}'.format(a,b))
print('-' * 30)
print('임시변수를 사용하는 방법\n')
temp = a
a = b
b = temp
print('a = {0}, b = {1}'.format(a,b))
print('-' * 30)
print('^(xor) 연산자를 이용하는 방법\n')
print('a = ', a, ":", bin(a))
print('b = ', b, ":", bin(b), '\n')
a = a ^ b
print('a = a ^ b = ', a, ":", bin(a))
b = a ^ b
print('b = a ^ b = ', b, ":", bin(b))
a = a ^ b
print('a = a ^ b = ', a, ":", bin(a), "\n")
print('a = {0}, b = {1}'.format(a,b))