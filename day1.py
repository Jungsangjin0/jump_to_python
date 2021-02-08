###숫자
#정수형
a = 123
a = - 178
a = 0

#float
a = 1.2
a = -3.45

#사칙연산
a = 3
b = 4
sum = a + b
mul = a * b
div = a / b
squared = a ** b
re = a % b
que = a // b

###문자
#문자열
"Hello World"
'Hello World'
"""hello world"""
'''hello world'''
"it's good"
'it"s good'
'it\'s good'
print('life is too short\nneed it')
print("""lief is too short
need it""")

#문자열 덧셈
head = "life is too short, "
tail = "need it "
print(head + tail)

#문자열 반복
print(tail * 2)

#문자열 길이
print(len(tail))
print(len("you need python"))


###문자열 인덱싱과 슬라이싱
#인덱스 시작은0
#-0 과 0은 같은 값 따라서 -1부터가 뒷 값
a = "life is too short, you need python"
print(a[3]) #e
print(a[-1])#n
#슬라이싱
#첫 자리 시작 뒷 자리 미포함
print(a[0:4])
#뒷 자리를 쓰지 않는다면 끝까지
print(a[19:])
#0 부터 표현한 숫자자리까지
print(a[0 : 17])
#처음부터 끝까지
print(a[:])
#인덱스 -값도 가능
print(a[19:-7])

#pithon -> python
a = "pithon"
#p 뽑고 i 빼고 thon 뽑고
print(a[0] + "y" + a[2:])
print(a[:1] + "y" + a[2:])

#문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples" % number)
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))
#문자열 포맷 코드
# %s = 문자열 , %c = 문자 1개, %d = 정수, %f = 실수, %o = 8진수, %x = 16진수, %% 이스케이프 리터럴%
# %s는 뒷 값을 자동으로 문자열로 바꾸기 때문에 아래처럼 가능하다
print("%s" % 3)
print("%s" % 3.14)

#정렬과 공백
print("%10s" % "hi")#총 10자리 중에 8자리는 공백 나머지2자리가 hi로 채워진다 정렬은 오른쪽
print("%-10sjane" %"hi") # -10s-> 총 10자리중에 왼쪽정렬
#소수점 나타내기
print("%0.4f" %3.123123) #소수점 아래 4자리까지만
print("%10.4f" %3.12312344) #전체 길이가 10개인 문자열 공간에서 오른쪽 정렬 소수점 아래 4자리 까지만 .포함
print("%.4f" %3.223123123) #자리수는 정하지 않음

#format함수를 사용한 포맷팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
print("I ate {0} apples. so i was sick for {1} days".format(3, "three"))
#name = value 형태로 대입가능
print("I ate {0} apples. so i was sick for {day} days".format(10, day=3))

#왼쪽 정렬
# print("{0}") -> print("{0:<10}")
print("{0:<10}".format("hi"))
#오른쪽 정렬
print("{0:>10}".format("hi"))
#가운데 정렬
print("{0:^10}".format("hi"))
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

#공백채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
#소수점 표현하기
print("{0:0.4f}".format(3.42134234)) #반올림됨
print("{0:10.4f}".format(3.42134234)) #자릿 수 10자리로 맞추기

#{또는} 문자 표현하기
print("{{ and }}".format())

#3.6 버전 부터 사용가능한 f문자열 포매팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
#표현식 사용가능
print(f"나의 이름은 {name}입니다. 나이는{age + 10}입니다.")
