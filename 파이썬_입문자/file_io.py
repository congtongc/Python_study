# open() : 파일을 특정한 모드로 여는 함수(읽을 때: r / 쓸 때: w)
# read() : 파일 객체로부터 모든 내용을 읽는 함수
# readline() : 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines() : 전체 내용을 한 번에 리스트에 담는 함수
# import os
# f = open(f"{os.getcwd()}\\텍스트_파일\\input.txt" , "r" , encoding = "UTF-8")
# # # f.seek(9)          # ()안에 숫자만큼의 byte를 건너뜀(3byte = 한글 1글자)
# # # data = f.read()
# # # print(data)
# # # f.close()

# # count = 0
# # while count < 3:
# #     data = f.readline()
# #     count = count + 1
# #     print("%d번째 줄 : %s" %(count, data), end = '')   
# # f.close()

# list = f.readlines()
# for i, data in enumerate(list) : 
#     print("%d번째 줄 : %s" %(i+1,data), end = '')
# f.close()
# # print(list)

# import os
# with open(f"{os.getcwd()}\\텍스트_파일\\input.txt", "r", encoding = "UTF-8") as f:
#     list = f.readlines()
#     for i,data in enumerate(list):
#        print("%d번째 줄 : %s" %(i+1,data), end = '')


# def process(filename):
#     with open(filename, "r") as f:
#         # 키 : 알파벳, 값 : 빈도수
#         dict = {}
#         data = f.read()
#         for i in data:
#             if i in dict :
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#     return dict
# dict = process("input.txt")