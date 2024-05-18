class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("홍길동")
student2 = Student("김철수")
print("인스턴스 student1의 이름 = ", student1.name)
print("인스턴스 student2의 이름 = ", student2.name)

print("인스턴스 student1의 타임 = ", type(student1))
print("인스턴스 student2의 타입 = ", type(student2))

class Student:
    def __init__(self, name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

student1 = Student("홍길동", "hong1234@email.net", "010-1234-5678")
student2 = Student("김철수", "kim1234@gmail.com", "010-3456-7890")
print("인스턴스 student1의 이름 = ", student1.name)
print("인스턴스 student1의 email = ", student1.email)
print("인스턴스 student1의 phone = ", student1.phone)
print()
print("인스턴스 student2의 이름 = ", student2.name)
print("인스턴스 student2의 email = ", student2.email)
print("인스턴스 student2의 phone = ", student2.phone)

class Student:
    def __init__(self, name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def to_print(self):
        return "{}\t{}\t{}".format(
            self.name, self.email, self.phone
        )
    
    def __del__(self):
        print(self.name, "객체가 소멸되었습니다.")
    
students = [
    Student("홍길동", "hong1234@email.net", "010-1234-5678"),
    Student("김철수", "kim1234@gmail.com", "010-3456-7890"),
    Student("홍길동", "hong1234@email.net", "010-2345-6789"),
    Student("김철수", "hong1234@email.net", "010-4567-7890")
]
print("이름","email","phone", sep = '\t\t')
print('-' * 50)

for student in students:
    print(student.to_print())

student1 = Student("김성결", "hong1234@email.net", "010-1234-5678")
print(student1.to_print())
del student1
print(student1.to_print())

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name
    def __gt__(self, other):
        return self.name > other.name
    def __ge__(self, other):
        return self.name >= other.name
    def __lt__(self, other):
        return self.name < other.name
    def __lle__(self, other):
        return self.name <= other.name
    
student = Student("김철수", 23)
student1 = Student("홍길동", 23)
print(student == student1)
print(student != student1)
print(student > student1)
print(student >= student1)
print(student < student1)
print(student <= student1)

class Registration:
    regi_num = 0        # regi_num => 클래스 변수
    def __init__(self, name):   # name => 인스턴스 변수
        self.name = name
        Registration.regi_num += 1
    def __del__(self):
        Registration.regi_num -= 1

student1 = Registration("홍길동")
student2 = Registration("김철수")

print(student1.name)
print(student2.name)
print(Registration.regi_num)
del student1
print(f"수강신청철회한 학생이 발생한 이후의 등록학생수 : {Registration.regi_num}")

class UnderSelf:
    def meth1(self):
        print("python 1")
    def meth2(self):        # => def meth2()는 선호하지 않음, 이렇게 사용할 경우 선언할 때 클래스 명으로 선언하여야 함(이 경우 Underself.meth2()로 해야함)
        print("python 2")

s1 = UnderSelf()
s1.meth1()
print('id(s1) = ', id(s1))
s1.meth2()   #  Underfself.meth2() => 이러한 방법도 있지만 선호하진 않음 