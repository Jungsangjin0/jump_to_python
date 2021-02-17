# while

# coffee
# coffee = 10
#
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈 {0}를 주고 커피를 줍니다.".format(money - 300))
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지않습니다")
#         print("남은 커피의 양은 {0}개 입니다.".format(coffee))
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# continue 를 이용해 while 처음으로 돌아가기


# 나혼자 코딩
# 1부터 10까지 3의 배수를 뺀 나머지 출력
# a = 0
# while a < 10:
#     a += 1
#     if a % 3 != 0:
#         print("{0}".format(a))
#     else:
#         continue


# for문
# 전형적 for문
test_list = ["one", "two", "three"]
for i in test_list:
    print(i)

# 다양한 for문 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print("first : {0}, last : {1}".format(first, last))

# range
# range(시작, 끝) = 시작부터 끝 전까지
# range(끝) = 0부터 끝 전까지0
a = range(10)
print(a)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

# 나 혼자 코딩
# for문 range 사용 1 ~100까지 더하기

add = 0
for j in range(1, 101):
    add += j
print(add)

# for range 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("{0} x {1} = {2}".format(i, j, (i * j)), end=" ")
    print('')

# for with list
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 간단하게
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 조건달아서
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
# [표현식 for 항목 in 반복 가능 객체 if 조건]

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)

# 연습문제
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)

numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)


# 함수
# def 함수이름(매개변수):
#   block

# 매ㅔ개변수 지정
def add(a, b):
    return a + b


result = add(a=3, b=7)
print(result)


result = add(b=6, a=3)
print(result)


#여러 개의 입력값
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5))

#키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)  #딕셔너리

print("print: {0}".format(print_kwargs(a=1))) #return 값이 없기때문에 None

def add_and_mul(a,b):
    return a+b, a*b

result1 = add_and_mul(3,4) # 튜플 값
# result1,result2 = add_and_mul(3,4) # 각각의 값
# print(result1, result2) #각각의 값
print(result1)

#매개변수 초깃값 미리설정
def say_myself(name, old, man=True):
    print("나의 이름은 {0}입니다".format(name))
    print("나의 나이는 {0}살입니다".format(old))
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응욕", 27) #초기값 설정으로 매개벼수를 전달하지않아도 된다


#def say_myself(name, old, man=True): 순서를 바꾸면 man을 읽지 못한다


def vartest(a):
    a += 1

print(vartest(3))
# print(a)


#함수 내에서 전역변수 사용 하기 : global


#lambda
#함수를 생성할 때 사용하는 에약어로 def와 동일한 역할을 한다
#lambda 매개변수1, 매개변수2, ...: 매개변수를 사용한 표현식
add = lambda a,b : a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a+b