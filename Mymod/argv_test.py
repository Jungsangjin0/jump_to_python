import sys
print(sys.argv)
#터미널에서 실행하면
# 그 값들이 python 뒤 명령어 들이 공백을 기준으로 sys.argv 의 리스트 요소가 된다.
#(python) E:\python\Mymod>python argv_test.py you need python
#['argv_test.py', 'you', 'need', 'python']

#자신이 만든 모듈 불러와 사용하기
#sys.path
#모듈들이 저장되어 있는 위치를 나타낸다.
print(sys.path)

#모듈 라이브러리 폴더에 추가하기
# sys.path.append("E:\\python\\Mymod")


#pickle
#객체의 형태를 그대로 유지하면서 파일에 저장하고 불러오기 가능
#pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
#어떤 자료형이든 저장할 수 있다
import pickle
f = open("text.txt", "wb")
data = {1 : "python", 2 : "you need"}
pickle.dump(data, f)
f.close()

f = open("text.txt", "rb")
data = pickle.load(f)
print(data)

#os
#환경 변수나 디렉토리, 파일 등의 os자원을 제어할 수 있게 해주는 모듈
#내 시스템의 환경 변수 값을 알고 싶을 때 os.environ
import os
print(os.environ) #딕셔너리 형태로 리턴
print(os.environ["PATH"]) # path print

#디렉토리 위치 변경하기
#os.chdir change dir
#현재 디렉터리 위치를 변경할 수 있다


#디렉토리 위치 돌려받기
#현재 자신의 디렉토리 위치를 돌려준다
#os.getcwd
print(os.getcwd())

#시스템 명령어 호출하기
#os.system
#시스템 명령어 dir 실행
print(os.system("dir"))

#실행한 시스템 명령어의 결과 돌려받기
#os.popen
f = os.popen("dir")
print(f.read())

#os.mkdir(디렉토리) 디렉터리를 생성한다
#os.rmdir(디렉토리) 디렉터리를 삭제한다. 단 디렉토리가 비어있어야 한다
#os.unlink(파일이름) 파일을 지운다
#os.rename(src, dst) src라는 이름의 파일을 dst라는 이름으로 바꾼다
os.rename("read.txt", "all.txt")

#shutil
#파일을 복사해 주는 파이썬 모듈
