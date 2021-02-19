##day7

# 클래스변수

class Family:
    lastname = "김"


# 클래스이름.클래스변수
print(Family.lastname)  # 김

# 객체를 통한 접근
a = Family()
b = Family()

print(a.lastname)  # 김
print(b.lastname)  # 김
print(id(a.lastname))
print(id(b.lastname))
print(id(Family.lastname))

# 클래스변수 값을 바꿀 경우 A,B 모두 바뀐다
Family.lastname = "박"
print(a.lastname)  # 박
print(b.lastname)  # 박
# 객체 a 의 값 변경
a.lastname = "정"
print(a.lastname)  # 정
print(b.lastname)  # 박

Family.lastname = "최"
print(a.lastname)  # 정
print(b.lastname)  # 최

print(id(a.lastname))  # 22171710 38336
print(id(b.lastname))  # 22171710 38416
print(id(Family.lastname))  # 22171710 38416

a.lastname = "chio"
b.lastname = "jung"
Family.lastname = "alie"
print(a.lastname)
print(b.lastname)
print(Family.lastname)
print(id(a.lastname))  # 2217166258928
print(id(b.lastname))  # 2217166259696
print(id(Family.lastname))  # 2217171034352

# 객체 생성 후 그 객체의 클래스변수의 값을 변경한다면
# 서로다른 주소 값을 가지게 된다
# 즉, 변경 전에 Family.lasname 과 a.lastname,b.lastname은 같지만
# a.lastname의 값을 변경하면 Family.lastname, Family.lastname과 다른 값을 가진다
# Family.lastname을 변경하면 a,b 둘다 바뀜
# a값을 바꾸면 family를 변경해도 안바뀜.
# a, b 변경 후 family를 변경해도 a,b 값 변경안됨


# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파일
# .py로 만든 파일은 모두 모듈

# import 모듈이름(파일이름) // mod1.add()
# mod1.add 쓰지않고 add처럼 쓰고 싶을 때
# from 모듈이름(파일이름) import 모듈함수(메소드)
# 모듈 내 모든 메소드 쓰고 싶을 때
# from 모듈 import 메소드, 메소드
# from 모듈 import *

# import mod1
# print(mod1.add(3, 4)


#모듈은 동일한 디렉토리 안에 있어야 한다
#혹은 라이브러리가 저장된 폴더에 있어야 한다
#모듈 내 변수, 클래스 메소드 사용
#터미널에서 setPYTHONPATH = C:\doit\mymod(폴더위치)
import mod2
print(mod2.PI) #모듈 내 변수
a = mod2.Math() # 모듈 내 클래스
print(a.solv(2)) # 모듈 내 클래스 내에 있는 함수
print(mod2.add(mod2.PI, 4.4)) #모듈 내 함수

