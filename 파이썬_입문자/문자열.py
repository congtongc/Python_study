# -*- Encoding : utf-8 -*-      한글 문자 출력을 위해 적어야 함
# a = "electric shock"
# b = " thunder "
# ctrl+/는 주석 사용
# "-(정수)" 는 문자열의 뒤부터 문자 표시
# ":" 끝 번호의 문자는 포함 안 함
# print(a[2:8:2])      2번째부터 8번째까지 2칸씩 띄어서
# b = a.replace("electric","phygical") 
# print(b)             electric을 phygical로 변경(replace함수)
# print(a.count('c'))  c의 개수확인(count함수)
# print(a.find("ric")) ric의 문자 위치 확인(find함수)
# print(a.upper()) 문자열을 모두 대문자로 변경(upper함수)
# b = a.lower() 
# print(b)    문자열을 소문자로 변경
# b = a.strip("electric")   
# print(b)       electric을 지운 문자열  
# b = a.split(" ")
# print(b)       각 문자열들을 배열로 나눔
# b = a.zfill(30)   
# print(b)    숫자만큼의 문자열을 나열하고 초과하면 앞을 0으로 채움(숫자를 셀때 주로 사용)
# a = "1000"
# b = int(a)
# print(b+206)   int 숫자 출력

# a = 57
# b = 35.7           숫자 연산은 실수와 정수도 가능하다 
# c = int(2903)      문자열과 숫자는 서로 연산이 불가하다 
# print(a+b+c)       문자열과 숫자는 서로 다르다.
# a = 0xFFFFFFFF
# print(a)           16진수 출력
# a = 11
# b = 21                     크기 제한 없음
# print("a+b = ", a+b)
# print("a-b = ", a-b)       연산 기호 사용
# print("a*b = ", a*b)       
# print("a/b = ", a/b)       나눗셈 실수까지, 
# print("a//b = ", a//b)     "//" 를 사용하면 몫만 출력
# print("a%b = ", a%b)       "%" 나누기를 한 나머지 값 출력
# a = (1+2j)
# b = (3+4j)                 복소수 연산도 가능
# print(a*b)

# a = 2                    " >> " , " << " 는 시프트 연산자로 숫자의 수만큼
# print(a >> 1)            각 방향으로 자리를 이동함
# a = 2                    
# b = 10                   " ** " 는 거듭제곱을 할 수 있음
# print(a ** b)            " = " 는 오른쪽에 있는 값을 왼쪽에 할당함
# a = 5                    " == " 는 왼쪽과 오른쪽의 값이 같음
# print(a == 5)            만약 양쪽의 값이 다를 경우 "FALSE"

# a = input()              파이썬 파일을 돌린 후에 input값에 문자열을 입력하면
# print(a)                 print함수에서 입력한 값을 출력
# a = input().split(' ')
# x = int(a[0])            input에 입력받은 값을 서로   
# y = int(a[1])            
# print("x+y=",x+y)        더하거나
# print("x-y=",x-y)        빼거나
# print("x*y=",x*y)        곱하거나
# print("x/y=",x/y)        나누어서      print함수를 통해 그 값을 출력

# A = 10                   A가 10이라는 곳을 가리키는 것을 의미함
# A = None                 A가 None이라는 곳을 가리키는 것을 의미함
# print(A+10)              None과 산수는 불가함으로 이 코드는 Error가 발생

# 리스트 : 비슷한 성질을 가진 객체의 나열
# 인덱스 : 0    1   2   3   4   5
#   값   :3.5  4.3  2.3 3.8 3.2 4.5
# a = [3.5, 4.3, 2.3, 3.8, 3.2, 4.5]    각 인덱스 별 값
# print("인덱스 0 = ", a[0])            "인덱스 0" 의 값 출력
# print("인덱스 1 = ", a[1])            "인덱스 1" 의 값 출력
# print("인덱스 2 = ", a[2])            "인덱스 2" 의 값 출력
# print("인덱스 3 = ", a[3])            "인덱스 3" 의 값 출력
# a[0] = 0.9                            "인덱스 0" 의 값 변경
# print("인덱스 0 = ",a[0])             변경된 "인덱스 0"의 값 출력    
# sum = 0                               sum이라는 변수에 기본 0 입력
# for i in a:                           반복문 for 사용( 'a' 배열 안의 변수 'i')
#     sum = sum + i                     sum이라는 변수에 'a' 배열 안의 변수 'i'의 값들을 더함
# print("평균 점수: ",sum/len(a))       len함수(length함수)를 사용, 평균 값 출력

# a = [
#     [90,95,87,67,88,92,40,56,89,71],
#     [77,54,53,87,41,99,64,91,60,81]
# ]
# sum = 0
# english = a[0]
# for i in english:
#     sum = sum + i
# print("영어 평균 점수 : ", sum / len(english))
# sum = 0
# math = a[1]
# for i in math:
#     sum = sum + i
# print("수학 평균 점수 : " , sum / len(math))

# a = [10,20,30,40,50,10,10]
# b = [70,50,40]
# count(원소) : 리스트 내 특정 원소가 몇 개 포함되어 있는지 반환
# print(a.count(10))
# index(원소) : 리스트 내 특정 원소의 인덱스를 반환
# print(a.index(50))
# append(원소) : 리스트의 뒤쪽에 새로운 원소를 삽입
# a.append(25)
# print(a)
# sort() : 리스트를 오름차순으로 정렬
# a.sort()
# print(a)
# extend(리스트) : 리스트의 뒤쪽에 다른 리스트를 삽입
# a.extend(b)
# print(a)
# insert(인덱스, 원소) : 특정한 위치에 원소를 삽입
# a.insert(3, 70)
# print(a)
# remove(원소) : 리스트 내 특정 원소를 삭제(단, 리스트의 앞에서부터 삭제)
# a.remove(10)
# print(a)
# pop(인덱스) : 리스트 내 특정 인덱스의 원소를 삭제
# a.pop(3)
# print(a)
# reverse() : 리스트의 앞뒤를 반대로 뒤집음
# a.reverse()
# print(a)

# 첫 명렬어는 들여쓰기 없이 시작
# 조건문, 반복문 등의 문법을 사용할 때는 콜론(:)으로 명령어의 끝을 알림
# 콜론(:)의 다음 줄부터는 들여쓰기의 간격이 모두 일정

# score = 100                           
# if score >= 80:                       if문을 사용하여 조건 설정
#     print("Good")                       조건에 맞으면 출력되는 내용
#     print("점수가 80점을 넘었습니다.")    (들여쓰기 필수!!)
# elif score >= 70:                     elif를 사용하여 다른 조건 설정
#     print("Not Bad")                    또한 조건에 맞으면 내용 출력
#     print("점수가 70점 이상입니다.")       (들여쓰기 필수!!)
# else:                                 else를 사용하여 또 다른 조건 설정
#     print("Bad")                         똑같이 조건에 맞으면 내용 출력 
# print("어떤 내용")                     이 내용은 조건문과 별개로 출력(들여쓰기X)
# if score < 90 and score >= 80:        조건문을 설정할때에 조건을 여러개 설정할 수있는데
#     print("Good")                       그때에는 연산(and,or,not,...)을 사용하여 조건문 설정

# list = [1,2,3]                            
# if 2 in list:                             
#     print("2가 리스트에 포함되어 있습니다.")  

# import keyword                예약어의 목록을 볼 수 있음
# print(keyword.kwlist)

''' 
작은 따옴표 3개로 여러 줄의 내용도 주석 처리가 가능하다. 
print("안녕하세요")
'''

