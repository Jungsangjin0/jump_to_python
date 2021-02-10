#day2

#딕셔너리사용법
d = {"name" : "홍길동", "age" : 30}
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")

#기본정렬
print(f"{'hi':<10}")
print(f"{'hi':>10}")
print(f"{'hi':^10}")

#공백채우기
print(f"{'hi':=<10}")
print(f"{'hi':!^10}")
print(f"{'hi':=>10}")

#소수점 표시
y = 3.32134234
print(f"{y:0.4f}")
print(f"{y:10.4f}")

print(f"{{and}}")

#나혼자 코딩
#format함수 또는 f문자열 포매팅을 사용해 "!!!python!!!" 문자열을 출력해보자
print(f"{'python':!^12}")
print("{0:!^12}".format("python"))


#문자열 관련 내장함수
#문자열 내 b 카운트
a = "hobby"
print(a.count('b'))

#위치 알려주기 find
a = "python is the best choice"
print(a.find("b"))
#값이 없을 경우 -1 반환
print(a.find("k"))

#index
a = "life is too short"
print(a.index("t"))
#index함수는 없을 경우 오류를 발생시킨다
#print(a.index("k"))

#문자열삽입
print("이부분")
print(",".join("abcd"))
#리스트에 추가
print(" ".join(['a','b','c','d']))

#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())
#소문자로 바꾸기
a = "HI"
print(a.lower())

#공백지우기
a = " hi "
#왼쪽 공백 지우기
print(a.lstrip())
#오른쪽 공백
print(a.rstrip())
#모두 지우기
print(a.strip())


#문자열 바꾸기
a = "life is too short"
print(a.replace("life", "your leg"))

#문자열 나누기 split
a = "Life is too short"
print(a.split()) #공백을 기준으로 나누어줌(스페이스, 탭, 엔터) 리스트로 나누어줌
b = "a:b:c:d"
print(b.split(":"))


###리스트 []
#비어있는 리스트 생성 방법
a = []
a = list()
print(a)

#리스트 내에 데이터는 자유롭게 가능
c = [1,2, 'life', 3.12]
print(c)

#리스트 내 리스트생성 가능
e = [1, 2, ['life', 'too']]

###리스트 인덱싱과 슬라이싱
a = [1,2,3]
print(a[0])
print(a[0] + a[2])
#뒤에서 부터 나타낼 때는 -1
print(a[-1])

a = [1,2,3, ['a', 'b', 'c']]
print(a[0])
print(a[3])
print(a[-1])
#리스트 내 리스트 값 가져오기
print(a[3][0])

a = [1, 2, ['a', 'b', ['life', 'is']]]
print(a[2][2][0])

#슬라이싱
a= [1, 2, 3, 4, 5]
print(a[0:2])

#구간까지 자르기
print(a[:2])
#마지막까지 자르기
print(a[2:])

#나혼자 코딩
# 리스트에서 슬라이싱 기법을 사용하여 [2.3] 나타내기
a = [1, 2, 3, 4, 5]
print(a[1:3])

#리스트 내 리스트 자르기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[3][:2])

#리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

#리스트 반복하기
print(a * 2)

#리스트 길이 구하기
print(len(a))

#문자열로 바꿔주는 내장함수
print(str(1) + "hi")

###리스트 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

#리스트 값 제거
#del 객체
#객체란 파이썬에서 사용되는 모든 자료형
del a[1]
print(a)

#슬라이싱을 이용한 리스트요소 한번에 삭제
a = [1,2,3,4,5]
del a[2:]
print(a)

#list append 함수
a = [1,2,3,4]
a.append(5)
print(a)
#list에 list 추가
a.append([1,2])
print(a)

#정렬함수
a = [1, 3,2, 4]
a.sort()
print(a)
b = ["a", "c", "d", "e"]
b.sort()
print(b)

#list 뒤집기 reverse
a = ['a', 'c', 'b']
a.reverse()
print(a)

#리스트 위치반환
a = [1,2,3]
print(a.index(3)) #3이 있는 인덱스 값 반환
print(a.index(2))
# print(a.index(4)) #없으면 오류

