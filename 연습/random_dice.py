import random
import time

def dice():
    MAX = 20
    # 최대로 시도 가능한 횟수를 질문
    print('*입력 가능한 횟수 : 1 ~', MAX , '회*')
    k = int(input('최대 시도 횟수를 입력하세요 : '))

    # 시도 횟수 제한(MAX에 지정된 횟수만큼)
    if(0<k<=MAX):
        MAX_SIZE = k
        i = 0
        j = 0
        List = list(0 for i in range(0,MAX_SIZE))
        while i != 6:
            i = random.randint(1,6)
            List.insert(j,i)
            time.sleep(0.8)
            print(i)
            j += 1    
            if j == MAX_SIZE:
                break
        if i == 6:    
            print('-->', i ,'(으)로 탈출!')
        else:
            print('-->', i ,'(으)로 실패...')
        print('나온 주사위 숫자 : ', List[0:j], ' 시도 횟수 : ', j,'회')
        quest()
    # 잘못된 값을 입력 시 다시 입력
    else:
        print('다시 입력하세요!\n')
        time.sleep(0.3)
        dice()

def quest():
    s = int(input('다시 하시겠습니까?(1(y)/0(n)) : '))
    if s == 1 : 
        dice()
    elif s == 0 :
        print('프로그램을 종료합니다.')
    else :
        print('잘못된 입력입니다.')
        quest()

dice()