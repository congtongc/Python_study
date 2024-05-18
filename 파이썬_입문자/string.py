# 문자열 자료형 뒤집기 : 슬라이싱 활용
# len() : 문자열의 길이를 출력
# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(), lower() : 문자열을 대문자로 혹은 소문자로 변환해주는 함수
# strip() : 좌우로 특정한 문자열을 제거하는 함수
# eval() : 문자열 수식 계산해주는 함수

# str = "Hello World"
# # print(str[::-1])      # 슬라이싱으로 자료형 뒤집기    
# print(len(str))         # len()으로 문자열의 길이 출력

# str = "HelloWorld"      # 문자로만 이루어져 있으면 True
# print(str.isalpha())    # 문자로만 이루어져 있지 않으면 False

# str = "123456"            # 숫자로만 이루어져 있으면 True
# print(str.isdigit())      # 숫자로만 이루어져 있지 않으면 False

# str = "abc 123"             # 문자와 숫자로만 이루어져 있으면 True
# print(str.isalnum())        # 문자와 숫자로만 이루어져 있지 않으면 False

# list = ['Hello', 'World', '홍길동']  # list의 내용
# print(',' .join(list))               # ','로 자료형들을 구분지어 합쳐서 출력

# str = "helloworld"            
# list = sorted(str)            # 오름차순으로 각 문자들을 정렬
# # print(list)                 # 오름차순으로 각 문자들을 정렬하여 출력
# print(''.join(list))          
# list = sorted(str, reverse = True)  # 내림차순으로 각 문자들을 정렬
# print(''.join(list))          

# str = "I wanna watch a movie."
# list = str.split(' ')       # 토큰에 따라 문자열을 구분하여 출력
# print(list)

# str = "I want you"       # 찾는 문자열의 첫 문자가 몇번째 인덱스인지 출력(찾는 문자열이 여러개인 경우 첫번째 문자열을 기준)
# print(str.find('like', 5))  # 찾는 문자열이 없으면 '-1' 출력   # 뒤에 숫자에 해당하는 번째수의 인데스 이후부터 문자열을 찾음

# str = "Hello World"
# print(str.upper())          # 대문자로 변경하여 출력
# print(str.lower())          # 소문자로 변경하여 출력

# str = "ttHello Worldtt"       # lstrip() : 왼쪽 문자열만 제거 / rstrip() : 오른쪽 문자열만 제거
# print(str.strip('t'))          # ()안에 있는 문자열을 str문자열에서 좌우로 제거

# exp = "(203+703)*3 - (30/6)"
# print(eval(exp))