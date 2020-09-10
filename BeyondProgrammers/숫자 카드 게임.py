# 참고 : https://rfriend.tistory.com/tag/2차원 배열 행 축으로 정렬 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]

import numpy as np

N, M = map(int, input("N, M을 띄워쓰기 하여 입력 : ").split())
li = [list(map(int, input("이차원 배열을 입력 : ").split())) for _ in range(N)]

li = np.array(li)
li = np.sort(li, axis=1)[::-1]
answer = li[0][0]

print(li)
print("정답 :", answer)