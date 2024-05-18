# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
# list = ['A','B','C','D','E']
# print(list.index('C'))       # 존재하지 않는 원소를 찾을 경우 오류 발생

# reverse() : 리스트 원소를 뒤집기
# list = [1,2,3,4,5]
# # list.reverse()
# # print(list)
# list = list[::-1]      # 슬라이싱을 사용하여 뒤집기
# print(list)

# sum(리스트 자료형) : 리스트의 모든 원소의 합
# list = [1,2,3]    # 문자열이 리스트 안에 존재할 경우 sum() 출력시 오류 발생
# print(sum(list))  # 리스트 안에 실수가 존재할 경우 정상 출력

# range(시작, 끝) : 특정 범위를 지정[(끝-1)한 범위까지 출력]
# my_range = range(5, 10)              # 범위를 지정함
# # print(my_range)                   # 범위가 잘 지정되었는지 확인
# list = list(my_range)               # list의 범위를 지정
# print(list)                         # list를 출력

# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환
# all() / any() : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
# list = [True, False, True]
# # print(all(list))                # 모든 원소가 참일 경우 True / 아니면 False
# print(any(list))                  # 원소 중 하나라도 참일 경우 True / 아니면 False

# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
# my_list = ['A', 'B', 'C', 'D', 'E']
# # result = list(enumerate(my_list))
# # print(result)
# for i,k in enumerate(my_list):
#     print("인덱스: ",i, " / 원소: ",k)

# sort() : 리스트의 원소를 정렬(오름 차순)
# my_list = ['A','B','C','D','E']
# my_list.sort()
# print(my_list)

# count() : 리스트에서 특정한 원소의 개수를 추출
# my_list = ['A','B','C','B']
# print(my_list.count('B'))

# del : 리스트의 특정 원소를 제거
# insert() : 리스트의 특정 원소를 삽입
# append() : 리스트의 가장 마지막 원소로서 원소를 삽입
# my_list = ['123','456','789']
# # # del my_list[1]            # 특정 원소 1개만 제거
# # del my_list[1:3]            # 특정 범위 내 원소를 모두 제거
# # my_list.insert(3,'-1')      # (어떤 위치, '어떤 원소')를 삽입할지 입력
# my_list.append('-1')          # 리스트의 가장 마지막에 입력한 원소를 삽입
# print(my_list)