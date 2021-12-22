x = 100

#  'x is 100'
print('x is' , x)

# 포맷 지시자를 포함한 문자열 % (객체)
print('x is %d' %(x))   # %d : 정수 / %f : 실수 / %s : 문자열

# f - string
print(f'x is {x}')

# 문자열의 format 매서드
print('x is {}'.format(x))

cnt = 5
# %,f - string, str.format을 사용하여 다음 출력
# I eat 5 apples.
print('I eat %d apples.' %(cnt))             # % 사용
print(f'I eat {cnt} apples.')                # f - string 사용
print('I eat {} apples. '.format(cnt))       # str.format 사용

A = 10
B = 15
# 10 + 15 = 25
print('%d + %d = %d' %(A,B,A+B))             # % 사용
print(f'{A} + {B} = {A+B}')                  # f - string 사용
print('{} + {} = {}'.format(A,B,A+B))        # str.string 사용

X = (A,B,A+B)
print('{0} + {1} = {2}'.format(*X))             # argument unpack

item = ('Apple' , 1000 , 'Red')
# Apple : Color is Red, Price is 1000 
print('{} : Color is {} , Price is {}'.format('Apple' , 'Red' , 1000))
print('{} : Color is {} , Price is {}'.format(item[0] , item[2] , item[1]))
print('{0} : Color is {2} , Price is {1}'.format(*item))   # .format('Aplle' , 'Red' , 1000)

A = 3.145592
B = 123.789
C = 12.423
# 소수점 아래 2개까지 출력
# %X.2f, {:X.2f}, {A:X.2f}를 사용   # 반올림    # X : 전체 자릿수
# 'A is 3.15' 와 같이 출력
print('A is %6.2f' %(A))
print(f'B is {B:6.2f}')
print('C is {:6.2f}'.format(C))

# 자릿수 지정하여 정수  출력
A = 1
# %02d : 두 자리의 정수로 문자열 만들기     # 앞에 숫자 0을 입력함으로써 빈 공간에 0을 입력
# A를 두자리로 출력
# 'A is 01'
print('A is %02d' %(A))
print(f'A is {A:02d}')
print('A is {:02d}'.format(A))
