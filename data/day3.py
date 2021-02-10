##day3

#list관련 함수

#리스트 요소 삽입
#insert(a, b) a위치에 b 삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

#list 요소 제거
a = [1, 2, 3, 1, 2, 3]
#첫 번째로 나오는3을 삭제한다
a.remove(3)
print(a)
a.remove(3)
print(a)

#list (맨 마지막)요소 끄집어 내기
a = [1, 2, 3]
print(a.pop())

#index 1 에 해당하는 요소 끄집어 내기
a = [1, 2, 3]
print(a.pop(1))

#list에 포함된 요소 x 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

#리스트 확장 extend list만 올 수 있다
a = [1, 2, 3]
a.extend([4, 5])
print(a)
#동일
a = [1, 2, 3]
a += [4, 5]
print(a)

###튜플 자료형
# 튜플은 ()로 감싼다
# list는 생성,수정,삭제가 가능하지만 튜플은 그 값을 바꿀 수 없다
t1 = ()
#한가지 요소만 가질 때는 반드시 뒤에 콤마가 붙어야 한다
t2 = (1,)
t3 = (1, 2, 3)
#괄호를 생략해도 무관하다
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
# del t1[0] del함수를 통한 삭제 불가능
# t1[0] = 'c' index 접근하여 값 변경 불가능

#튜플 인덱싱
print(t1[0])
#슬라이싱
print(t1[0 : 3])
#튜플 더하기
t2 = (3, 4)
print(t1 + t2)
#곱하기
print(t1 * 2)
#길이 구하기
print(len(t1))

#나혼자코딩
#(1,2,3)이라는 튜플에 값 4를 추가하여 출력하기
t1 = (1, 2, 3)
#튜플을 추가 할 시 에는 반드시 콤마를 찍자
t1 += 4,
#찍지 않으면 t1 에 4가 들어가서 4만 출력된다
print(t1)


###딕셔너리 자료형 {}를 사용하여 표현
#key에는 변하지 않는 값 value에는 변하는 값 변하지않는 값 둘 다
a = {'a' : [1,2,3]}
a = {1 : "hi"}
a = {1 : (1, 2, 3)}

#딕셔너리에서 [] 안에 들어가는 값은 index가 아닌 key 값이다.
#딕셔너리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b' # {2 :"b"} 쌍 추가
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[1] #키값 삭제
print(a)

#딕셔너리 key 중복 불가
#맨 마지막 꺼만 읽히는 듯 -
a = {1 : 'a', 1 : "b", 1 : "c"}
print(a)

a = {(1, 2) : 1}
print(a[(1, 2)])

#딕셔너리 관련 함수
#딕셔너리 키 값 조회
#a의 key만을 모아서 dict_keys 객체를 돌려준다
a = {'name' : 'pey', 'phone' : '01101110111', 'birth' : '1118'}
print(a.keys())

#기본적으로 iterate 사용가능

#key값들을 list로 나타내기
print(list(a.keys()))

for k in a.keys():
    print(k)

#value 값 뽑기
print(a.values())

# key, value 쌍 얻기
#튜플로 반환
print(a.items())

# key value 쌍 모두지우기
a.clear()
print(a)


#key로 value 얻기 get
a = {"name" : "pey", "phone" : "101101212", "birth" : "1118"}
print(a.get("name"))
print(a["name"])

#a["dasd"] -> 키가없다면 오류를
#a.get("ads") -> None을 return 함

#get 디폴트 값 설정
#a.get('foo', 'bar') bar-> default
print(a.get('foo', 'bar'))


#딕셔너리 key값 존재하는 지 찾기 (in)
print('name' in a)
print("pep" in a)

#나 혼자 코딩
dic = {"name" : "홍길동", "birth" : "1128", "age" : 30}

#집합 자료형
#중복을 허용하지 않는다
#순서가 없다
s1 = set([1, 2, 3])
print(s1)

s2 = set("hello")
print(s2)

#set자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환해야한다
s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])

#set 자료형을 유용하게 사용할 때는 교집합, 합칩합, 차집합을 구할 때
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)
#교집합 함수
print(s1.intersection(s2))
#합집합
print(s1 | s2)
print(s1.union(s2))
#차집합
print(s1 -s2)
print(s2 - s1)
print(s1.difference(s2))

#값 추가하기 add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
#값 여러개 추가하기 update
s1 = set([1, 2, 3])
s1.update([4,5,6])
print(s1)

#특정값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)