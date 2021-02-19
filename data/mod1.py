def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 직접 이 파일을 실행했을 때 if문이 참이 되어 실행된다
# 반대로 대화형 인터프리터나 다른 파일에서 이모듈을 불러서 사용시에는 거짓으로 실행안됨
# if __name__ == "__main":
if __name__ == "mod1":
    print("mod1 입니다~")
    print(add(3, 4))
    print(sub(4, 2))

# __name__변수란

# __name__은 내부적으로 사용하는 특별한 변수 이름
# 직접 mod1.py를 싱핼할 경우 mod1.py의 __name__변수에 __main__값이 저장된다
# 하지만 파있너 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우 __name__변수에는
# mopd1.py의 모듈 이름 값 mod1이 저장된다.
