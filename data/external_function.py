#sys
#파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
#자신이 만든 모듈 불러와 사용하기
#sys.path
#모듈들이 저장되어 있는 위치를 나타낸다.
import sys
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
# os.rename("read.txt", "all.txt")

#shutil
#파일을 복사해 주는 파이썬 모듈
# import shutil
# shutil.copy("src.txt", "dst.txt")
#src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉터리 이름이라면 src라는
#파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

#glob
#특정 디렉토리에 있는 파일 이름 모두를 알아야 할 때
print("glob")
import glob
print(glob.glob("E:\python\data\day*"))

#tempfile
#파일을 임시로 만들어서 사용할 때 유용한 모듈
#tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다
import tempfile
filename = tempfile.mktemp()
print(filename)
#tempfile.TemporaryFile()
#임시 저장 공간으로 사용할 파일 객체를 돌려준다
#이 파일은 기본적으로 바이너리 쓰기모드(wb)를 갖는다
#f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
import tempfile
f = tempfile.TemporaryFile()
f.close() # 생성한 임시파일이 자동으로삭제됨

#time
import time
print(time.time()) # 초단위로 알려줌

print(time.localtime())
print(list(time.localtime()))

#time.asctime
#localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기
#쉬운 형태로 돌려줌
print(time.asctime(time.localtime()))

#time.ctime
#ctime은 항상 현재 시간만 돌려준다
print(time.ctime())

#time.strftime
#time.strftime("포맷코드", time.localtime(time.time()))
#%a Mon 요일 줄임말
#%A Monay 요일
#%b jan 달 줄임말
#%B january 달
#%c 06/01/01 17:22:21 닐짜와 시간
#%d [01, 31] 날day
#%H [00, 23] 시간 24시간 형태
#%l [01, 12] 시간 12시간 형태
#%j [001, 365] 1년 중 누적 날짜
#%m [01, 12] 달
#%M [01, 59] 분
#%p AM AM OR PM
#%S [00, 56] 초
#%U 1년중 누적 주:일요일을 시작으로 [00, 53]
#%w 숫자로 된 요일 [0(일요일), 6]
#%W 1년 중 누적 주 -월요일 시작 [00, 53]
#%x 현재 설정된 지역에 기반한 날짜 출력 06/01/01
#%X 형재 설정ㄷ왼 ㅈ ㅣ역에 기반한 시간 출력 16:21:21
#%Y 연도출력 2001
#%Z 시간대 출력 대한민국 표준시
#%% 문자 %
#%y 세기 부분을 제외한 연도 출력 01


import  time
print(time.strftime("%x", time.localtime(time.time())))

#time.sleep
#일정한 시간 간격을 두고 루프를 실행할 수 있다
# for i in range(10):
#     print(i)
#     time.sleep(1) #1초

#calendar
#달력
#calendar.calendar(연도)
import calendar
print(calendar.calendar(2021))

#calendar.prcal(연도) 위와 같은 결과
print(calendar.prcal(2021))

#2021년 12월 달력만
print(calendar.prmonth(2021, 5))

#calendar.weekday
#weekday(연도, 월, 일)
#월요일0 일요일6
print(calendar.weekday(2021,2,22))

#calendar.monthrange
#monthrange(연도,월)
#1일이 무슨 요일인지, 달의 마지막 날짜
print(calendar.monthrange(2021, 2))

#ranodm
#난수
import random
print(random.random())
print(random.randint(1, 10))

#choice
#랜덤으로 하나 선택해줌
aa = [1, 2, 3, 4, 5]
print(random.choice(aa))

#shuffle 섞기
random.shuffle(aa)
print(aa)

#webbriwser
#자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
import webbrowser
# webbrowser.open("http://google.com")

#웹브라우저가 실행된 상태이더라도 새로운 창으로열리게
webbrowser.open_new("http://google.com")