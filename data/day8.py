# 예외처리

# try except

# try
# block
# except:
# 종류에 상관없이 처리
# except 발생오류:
# 발생오류에 대한 오류에 대해 처리
# except 발생 오류 as 오륲 메세지 변수:
# 오류 메세지의 내용까지 알고 싶을 때

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# f = open("foo.txt", "w")
# try:
# block
# finally:
#     f.close()

# try:
#     a = [1, 2]
#     print(a[3])
#     4/ 0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
#
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except (ZeroDivisionError, IndexError) as  e:
#     print(e)
# pass 오류 회피하기

# d오류 일부러 발생시키기
# raise
class Bird:
    def fly(self):
        raise NotImplementedError  # 반드시 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류 발생


class Engle(Bird):
    def fly(self):
        print("very fast")


engle = Engle()

print(engle.fly())


# 예외 만들기
class MyError(Exception):
    # pass

    # 오류 메세지 만들기
    def __str__(self):
        return "허용되지 않은 별명입니다." 
        #return 을 쓰지않으면 오류남

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")

except MyError as e:
    print(e)

# except MyError as e:
#     print(e)
    # print("허용되지 않는 별명입니다.")