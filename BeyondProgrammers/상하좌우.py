import sys


def direction():
    N = int(sys.stdin.readline())
    li = list(sys.stdin.readline().split())
    x, y = 1, 1  # 지도상에서의 좌표를 의미

    for i in range(len(li)):
        if li[i] == 'L' and y > 1:
            y -= 1
        elif li[i] == 'R' and y < N:
            y += 1
        elif li[i] == 'U' and x > 1:
            x -= 1
        elif li[i] == 'D' and x < N:
            x += 1
    print(x, y)
    return True


direction()

# x,y 헷갈려서 15분 걸림ㅠㅠ