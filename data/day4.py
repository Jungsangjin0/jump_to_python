###day4
a = True
b = False
print(type(a))
print(type(b))
print(1 == 1)
print(2 > 1)
print(2 < 1)

#자료형의 참과 거짓
print(bool("python")) #true
print(bool("")) #false
print(bool([1, 2, 3])) #true
print(bool([])) #false
print(bool(())) #false
print(bool({}))  #false
print(bool(0)) #false
print(bool(1)) #true
print(bool(None)) # false

#메모리
a = [1, 2, 3]
print(id(a)) #주소값 hash
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)  # a와 b가 같은 것을 볼 수 있다
a[1] = 4
print(a)
print(b) # 둘 다 변하는것을 볼 수 있다.

#list값만 복사하기
a = [1, 2, 3]
b = a[:] # list a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a)
print(b) #값만 복사했기 때문에

#copy 함수
from copy import copy
a = [1, 2, 3]
b = copy(a)

#복사
a = [1, 2, 3]
b = [1, 2, 3]
print(b is a)

#변수를 만드는 여러가지 방법
a, b = ("python", "life")
print(a, b)
print(type((a, b))) #tuple
(a, b) = "python", "life"
print((a, b))
print(type((a, b)))


[a, b] = ["python", "life"]
print([a, b])
a = b = "python"
print(a)
print(b)
print(a is b)

#값 switching
a = 3
b = 5
a, b = b, a
print(a)
print(b)

#연습문제
#Q1
ko = 80
en = 75
ma = 55
print((ko + en + ma) / 3)

#Q2
#자연수 13이 홀수인지 짝수인지
print((13 % 2 == 1) is True)

#Q3
pin = "881120-1068234"
print(pin[:6])
print(pin[7:])

#Q4
print(pin[7])

#Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#Q7
a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)

#Q8
a = (1, 2, 3)
a = a + (4, )
print(a)

#Q10
#key "B" 추출
a = {"A" : 90, "B" : 80, "C" : 70}
result = a.pop("B")
print(a)
print(result)

#Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

###if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")


#나 혼자 코딩
#주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라
pocket = ["card", "cip", "re"]
if "card" not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")
    
#아무일도 안하게 할 때 pass사용
#주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
pocket = ["paper", "money", "cellphone"]
if "money" in pocket:
    pass
else:
    print("카드를 꺼내라")

#elif
pocket = ["paper", "cellphone"]
card = True
if "money" in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

pocket = ["paper", "cellphone"]
card = True
if "money" in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#간결하게 사용하기
if "money" in pocket:
    pass
else :
    print("카드를 꺼내라")

pocket = ["paper", "money", "cellphone"]
if "money" in pocket: pass
else : print("카드를 꺼내라")

#조건부 표현식
score = 60
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

#간단히 표현하기
message = "success" if score >= 60 else "failure"
#조건문이 참인경우 if 조건문 else 조건문이 거짓인 경우
print(message)

