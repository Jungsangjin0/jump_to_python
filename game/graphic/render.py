# render.py

# import
# from game.sound.echo import echo_test

from ..sound.echo import echo_test
#..은 부모 디렉토리를 의미한다.
# graphic 과 sound 디렉터리는 동일한 깊이 이므로 부모 디렉토리(..)를 사용하여 위와 같이 import 할 수 있다

def render_test():
    print("rendaer")
    echo_test()
