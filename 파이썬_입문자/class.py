# 클래스(Class) : 반복되는 불필요한 소스코드를 최소화 하면서 
#                 현실 세계의 사물을 컴퓨터 프로그래밍 상에서 
#                 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
# 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수, 메소드라고 부름

# class Car:
#     # 클래스의 생성자     :     형태가 정해져있음{ex)__init__}   
#     def __init__(self, name, color):      # self : 기본으로 가지는 매개변수
#         self.name = name                  # 클래스의 멤버
#         self.color = color                # 클래스의 멤버
#     # 클래스 소멸자
#     def __del__(self):
#         print("인스턴스를 소멸시킵니다.")
#     # 클래스의 메소드
#     def show_info(self):
#         print("이름:", self.name, "/ 색상" , self.color)
#     # Setter 메소드
#     def set_name(self, name):
#        self.name = name

# car1 = Car("소나타" , "빨간색")
# car1.set_name("아반떼")
# car1.show_info()  
# del car1
# car2 = Car("아반떼", "검은색")
# car2.show_info()
# print(car1.name, "을(를) 구매했습니다!")


# 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법(부모와 자식 관계)
# 자식 클래스 : 부모 클래스를 상속 받은 클래스{show_info함수는 자식 클래스에서만 사용 가능(부모X)}
# 상속을 받은 자식 클래스가 부모 클래스와 동일한 변수나 메소드를 가진다면 자식 클래스를 우선 처리
# class Unit:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(self.name, "이(가) 공격을 수행합니다. [전투력 :",self.power, "]")

# # unit = Unit("홍길동", 375)
# # unit.attack()

# class Monster(Unit):
#     def __init__(self, name, power, type):
#         self.name = name
#         self.power = power
#         self.type = type
#     def show_info(self):
#         print("몬스터 이름 :", self.name, " / 몬스터 종류 :", self.type)

# monster = Monster("슬라임", 10, "초급")
# monster.show_info()
# monster.attack()
