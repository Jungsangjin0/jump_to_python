###day6

# 사용자 입력과 출력
# input()
# 입력받은 값은 문자열로 취급된다

# number = input("숫자를 입력하세요 : ")
# print(number)

print("Life""is""too short")
print("Life" + "is too " + "short")
print("Life", "is", "too", "short")


# 파일생성
# f = open("새파일.txt", "w")
# f.close()

# 파일 객체 = open(파일이름, 파일 열기모드)
# r -> 읽기모드- 파일을 읽기만 할 떄사용
# w -> 쓰기모드 - 파일에 내용을 쓸 때 사용
# a -> 추가모드- 파일의 마지막에 새로운 내용을 추가할 때 사용
# 파일을 쓰기 모드로 열면 해당 파일이 존재할 경우 원래 있던 내용이; 사라지고
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다
# 만약 새 파일을 다른 디렉토리에 생성하고 싶다면 다르게 작성해야 한다
# 위치 다 잘 쓰기

# f = open("E:/python/cgv/새파일.txt", "w")
# f.close()

# 쓰기
# 쓰기를 할 때는 print 가 적용되지 않기 때문에 \n 을 사용

# f = open("새파일.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     data  = "{0}번째 줄입니다.\n".format(i)
#     f.write(data)
# f.close()


# readline
# f = open("새파일.txt", "r")
# line = f.readline()
# print(line)
# for i in range(1, 11):
#     data = "{0}번째 줄입니다.\n".format(i)
#     f.write(data)
# f.close()
# utf-8을 쓰면 ide에서도 한글을 볼 수 있다
# 열때도 encoding="utf-8" 쓸때도 encoding="utf-8"을 써줘야 한다

# f = open("새파일.txt", "r")
# while True:
#     line = f.readline()
#     if not line: break #readline()은 더 이상 읽을 줄이 없으면 None을 뱉는다
#     print(line)
# f.close()

# readlines()
# 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다

# f = open("새파일.txt", "r")
# lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line)
# f.close()


# read()
# 파일의 내용 전체를 문자열로 돌려준다
# f = open("새파일.txt", "r")
# data = f.read()
# print(data)
# f.close()


# add data
# "r"을 사용할 경우 덮어쓰기 되지만 "a"할 경우 이어 써짐 append
# f = open("새파일.txt","a")
# for i in range(11,21):
#     data = "{0} 번째 줄입니다.\n".format(i)
#     f.write(data)
# f.close()


# close를 자동으로 닫아주는 구문
# with open("foo.txt", "w") as f:
#     f.write("Life is too short you need python")

# with문을 사용하면 with블록을 벗어나는 순간 열린 파일 객체가 자동으로 close된다

# sys


# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i)


# Q2
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)
#
#
# print(avg_numbers(1, 2))
# print(avg_numbers(1, 2, 3, 4, 5))


# Q3
# input1 = input("첫 번째 하나")
# input2 = input("두 번쨰 하나")
# total = int(input1) + int(input2)
# print("두 수의 합은 {0}이다".format(total))


# Q4
# f1 = open("test.txt", "w")
# f1.write("Life is too short")
# f1.close() #닫지않고 바로 ㅇ읽으려 하면 데이터를 읽을 수 없음

# f2 = open("test.txt", "r")
# print(f2.read())


###CLASS

# 객체와 인스턴스의 차이
# a= Cookie() a는 객체
# a객체는 Cookie의 인스턴스이다.


# 사칙연산 클래스

class FourCal:
    def __init__(self, first, second):  # 생성자
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def dov(self):
        result = self.first / self.second
        return result


# a = FourCal()
# a.setData(3, 4)
# 잘 사용하지않지만 다음과 같이 클래스를 통해 메소드 호출 가능
# a = FourCal()
# FourCal.setData(a, 4, 2)
# 위와 같이 "클래스.이름.메소드" 형태 호출할 때는 객체 a를 매개변수에 전달해줘야 한다
# 객체.메소드는 반드시 self 생략할 것
# a = FourCal()
# a.setData(4, 2)


# 각각의 객체는 독립적이다
# id()를 사용하여 객체(또는 값)의 주소를 알 수 있다.


# 상속
# class 클래스 이름(상속할 클래스 이름):
# 상속받은 클래스에서도 부모 클래스의 기능을 사용할 수 있다
# 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속해야한다
class MoreFourCal(FourCal):
    # 수정 시 생성자에 값이 더 들어갈 경우 아래와 같이 사용
    # def __init__(self, first, second, aa):
    #     FourCal.__init__(self, first, second)
    #     self.aa = aa
    
    #수정할 값이 없다면 init없이 사용가능(부모의 init)

    def pow(self):
        result = self.first ** self.second
        return result


# a = MoreFourCal(4, 2, 10) #수정 시 생성자에 값이 더 들어갈 경우 
a = MoreFourCal(4, 2)
print(a.pow())


##메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second