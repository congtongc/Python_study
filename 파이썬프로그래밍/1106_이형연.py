# 6-1
def print_10times_star():
    print('*' * 10)

print_10times_star()

# 6-2
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)

# 6-3
def plus(v1, v2):
    '''이 함수는 v1과 v2를 더한 뒤 결과를 반환하는 함수입니다.'''
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)
print(plus.__doc__)

# 6-4
def add_multi(n1, n2):
    return n1 + n2, n1 * n2

result = add_multi(5, 10)
print(result)

# 6-5
def two_times(n):
    return print(n * 2)

two_times(5)
two_times('abc')

two_times((1, 2, 3))
two_times((1, 2, 3))

# 6-6
def add_print(a, b):
    print("%d , %d의 합은 %d입니다." %(a, b, a + b))

add_print(1, 9)
hap = add_print(3, 4)
print(hap)      # 반환 받은 값 없이 출력만 함

# 6-7
def hi():
    return 'Hi 파이썬 프로그래밍'   # 입력 값은 없지만 반환 값은 있음

aha = hi()
print(aha)

# 6-8
def hi2():
    return print('Hi 파이썬 프로그래밍')    # 입력 값 & 반환 값 없음

hi2()

# 6-9
def student_info(name, phone, id_no = '비공개'):
    print('이름 : ', name)
    print('휴대폰 : ', phone)
    print('주민번호 : ', id_no)

student_info('김철수', '010 - 1234 - 5678')

# 6-10
def student_info(name, phone, id_no = '비공개'):        
    print('이름 : ', name)
    print('휴대폰 : ', phone)
    print('주민번호 : ', id_no)

student_info('김철수', '010 - 1234 - 5678', '2020101 - 3145312')

# # 6-11
# def student_info(name, id_no = '비공개', phone):                  # 기본 값이 지정되어 있는 변수 뒤로 기본 값이 지정되어 있는 변수는 위치할 수 없음(Syntax Error)
#     print('이름 : ', name)
#     print('휴대폰 : ', phone)
#     print('주민번호 : ', id_no)

# student_info('김철수', '2020101 - 3145312', '010 - 1234 - 5678')

# 6-12
def add_m(*args):
    result = 0
    for i in args:
        result = result + i
    return result

r1 = add_m(1, 2, 3)
print('r1 = ', r1)

r2 = add_m(1, 2, 3, 4)
print('r2 = ', r2)

r3 = add_m(1, 2, 3, 4, 5, 6)
print('r3 = ', r3)

# 6-13
def value_times(times, *values):        # 가변 매개 변수와 매개 변수 혼용 시 하나만 맨 뒤에 사용
    for value in values:
        print(times * value)

value_times(3, 1, 2, 3, 4, 5)

# 6-14
def f_a():
    num = 20        # 지역 변수
    print('f_a()의 num값 %d' %num)

def f_b():
    print('f_b()의 num값 %d' %num)

num = 10            # 전역 변수
f_a()
f_b()

# 6-15
def f_a():
    global num
    num = 20
    print('f_a()의 값 %d' %num) # 선언한 변수 사용(20)

num = 10        # 전역 변수 선언1(10)
f_a()           # 전역 변수 선언2(20) => 전역 변수 수정 가능
print('전역변수 num값 %d' %num) # 최종 전역 변수 출력(20)

# 6-16
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        if v2 == 0:
            return 'error'
        result = v1 / v2
    elif op =='**':
        result = v1 ** v2
    return result

res, var1, var2, oper = 0, 0 ,0, ''

while True:
    oper = input('연산자를 입력하세요(+, -, *, /, **, 종료 : q) : ')
    if oper == 'q':
        print('프로그램을 종료합니다.')
        break
    var1 = int(input('첫 번째 숫자를 입력하세요 : '))
    var2 = int(input('두 번째 숫자를 입력하세요 : '))
    res = calc(var1, var2, oper)
    if res == 'error':
        print('0으로 나누면 안됩니다.')
    else:
        print("## 계산기 : %d %s %d = %d" %(var1, oper, var2, res))

# 6-17
def add(n, m):
    return n + m

print('add함수 : ', add(2,5))

# 람다함수로 작성
print('lambda함수 : ', (lambda n, m : n + m)(2, 5))

# 6-18
# reduce()를 사용하지 않는 경우
product1 = 1
list = [1, 2, 3, 4]
for num in list:
    product1 = product1 * num
print('product1 = ', product1)

# reduce()를 사용하는 경우
from functools import reduce
product2 = reduce((lambda x, y : x * y), [1, 2, 3, 4])
print('product2 = ', product2)

# 6-19
from functools import reduce

def cube(y):
    return y * y * y

g = lambda x : x * x * x
print('print(g(7)) = ', g(7))

print('print(cube(5)) = ', cube(5))

# lambda함수와 함께 사용한 filter()함수
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print('li = ', li)
final_list_filter = list(filter(lambda x : (x % 2 != 0), li))
print('print(final_list_filter) = ', final_list_filter)

# lambda()함수와 함께 사용한 map()함수
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list_map = list(map(lambda x : x * 2, li))
print('print(final_list_map) = ', final_list_map)

string = reduce(lambda x, y : y + x, 'abcde')
print('print(string) = ', string)

# 람다함수
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_lambda = list(map(lambda x: str(x) if x % 2 == 0 else x, a))
print(f'a = {a}')
print('a_lambda = ', a_lambda)

b_lambda = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print('a_lambda = ', b_lambda)

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
    
c_lambda  = list(map(f, a))
print('c_lambda = ', c_lambda)