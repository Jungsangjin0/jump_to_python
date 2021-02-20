# 내장함수

# abs
abs(3)  # 절댓값

# all
# 반복 가능한 값을 인수로 받으며 x가 모두 참이면 true 하나라도 거짓이면 false
# 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것
# 리스트, 튜플, 문자열, 딕셔너리, 집합

print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))  # 0은 false

# any
# 하나라도 true 면 true 다 거짓이면 false
print(any([1, 2, 3, 0]))
print(any([0, ""]))

# chr
# 아스키코드 값을 입력받아 코드에 해당하는 문자 출력
print(chr(97))

# dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다
print(dir([]))

# divmod
# 2개의 인자를 받는다./ 그리고 a b를 나눈 몫과 나머지를 튜플 형태로 돌려준다 a 나누기 b
print(divmod(33, 3))

# enumerate "열거하다"
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)
    # i는 인덱스
    # name은 값

# eval
# eval(expression)은 실행가능한 문자열(1+2, "hi"+"a"같은 것)을입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
print(eval("1+2"))
print(eval("'hi' + 'a'"))
print(eval('divmod(3, 4)'))


# 문자열을 주면 그 값을 실질적인 값으로 실행 시켜줌
# 보통 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을때 사용

# filter
# 첫 번째 인수로 함수를, 두번 째 인수로 그 함수에 차례로 들어가 반복 가능한 자료형을
# 인수가 함수에 들어감녀서 반환 값이 참인 것만 묶어서 돌려준다
def positive(l):
    result = []  # 걸러내서 저장할 변수
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -3, 2, 0, -5, 6]))


# 간단하게 작성
def positiveA(x):
    return x > 0


print(list(filter(positiveA, [1, -3, 2, 0, -5, 6])))
# 람다식
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])) #list 사용 안하면 filter 객체로 반환

# hex
# hex(x)정수 값을 받아 16진수 hexadecimal 로 변환하여 돌려주는 함수
print(hex(234))

# id
# id(obj) 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 돌려주는 함수
a = 3
print(id(a))
print(id(3))
b = a
print(id(b))

# input
# input([prompt])
# a = input()

# int
# 문자열 형태의 숫자나 소숫점 숫자 등을 정수로 돌려줌
print(int("3"))
print(int(3.4))
# print(int(0xea, radix)) #?? radix진수로 표현된 문자열 x를 10진수로 변환
print(int("11", 2))  # 3
print(int("1A", 16))  # 26


# isinstance
# isinstance(object, class) 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 true, 거짓이면 false
class Person: pass


a = Person()
b = isinstance(a, Person)  # a가 Persion 클래스의 인스턴스인지 확인
print(b)
q = 3
print(isinstance(q, Person))

# len
# 입력값 s 의 길이
print(len("python"))
print(len([1, 2, 3]))

# list
# 반복 가능한 자료형 s를 받아 리스트로 만들어 줌
print(list("pyrthon"))
print(list((1, 2, 3)))


# map
# map(f, iterable) 함수 f 와 반복 가능한 자료형을 입력으로 받는다.
# map은 입력 받은 자료형의 각 요소를 함수 f 가 수행한 결과를 묶어서 돌려주는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)


# map함수 사용 시
def two_times2(x): return x * 2


print(map(two_times2, [1, 2, 3, 4])) #<map object at 0x0000026804709C70>
print(list(map(two_times2, [1, 2, 3, 4]))) #map의 결과를 리스트로 보여 주기 위해 list함수 사용
#lambda
print(list(map(lambda x : x * 2, [1, 2,3, 4])))

