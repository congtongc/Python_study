# 사전(dictionary) : 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
# dict = {}
# dict['안녕'] = 'Hello'
# dict['기적'] = 'Miracle'
# dict['노력'] = 'Effort'
# # print(dict)
# # i : 인덱스 , k : Key값
# # for i, k in enumerate(dict):
# #     print("[인덱스 : ", i, "] 한글 : ", k , "/ 영어 : ", dict[k])
# dict['안녕'] = 'Hi'  # 원하는 항목을 바로 변경할 수 있음
# # del dict['기적']   # del함수를 통해 특정 dictionary를 제거 가능
# # dict.clear()      # dictionary의 자료값을 모두 제거 
# # # print(dict)
# # print("사전 자료형의 길이 : ", len(dict))
# # keys = dict.keys()
# # key_list = list(keys)
# # values = dict.values()
# # value_list = list(values)
# # # print("키 : ", keys)
# # # print("키 리스트 : ", key_list)
# # print("값 리스트 : ", value_list)
# if '노력' in dict :
#     print("[노력] 키가 존재합니다. ")


# scores = {}
# scores['A'] = 78
# scores['B'] = 99
# scores['C'] = 85
# print(sorted(scores))       # 키(Key)로 정렬
# print(sorted(scores, reverse = True))       # 키(Key)를 내림차순 정렬
# print(sorted(scores.values()))  # 값을 정렬하기
