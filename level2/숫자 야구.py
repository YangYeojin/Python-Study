from itertools import permutations


def checking(number, QnA):
    number = list(number)
    q0 = list(str(QnA[0]))
    strike, ball = 0, 0
    for j in range(3):
        if number[j] == q0[j]:
            strike += 1
        elif q0[j] in number:
            ball += 1
    if strike == QnA[1] and ball == QnA[2]:
        return True
    return False


def solution(baseball):
    numlist = list(map(''.join, permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)))
    for i in baseball:
        for num in numlist[:]:
            if not checking(num, i):
                numlist.remove(num)
    return len(numlist)


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))


'''
# 순열이랑 조합 공부하다가 조합 함수를 직접 짜는 코드를 발견했는데 'yield'라던가 'generator'에 대해 설명해주고 있어서 신기해서 가져와봤어요
# 코드 짤 때 가끔 < ~~~~ object generator at 0X00000217876AEBa0> 이런 거 보이는데 이게 뭔지 알려줘요
# https://blog.naver.com/PostView.nhn?blogId=kmh03214&logNo=221685090465&parentCategoryNo=&categoryNo=26&viewDate=&isShowPopularPosts=true&from=search
# 조합 함수
def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:  # 종료조건
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r - 1):
                yield [arr[i]] + next


pr = list()
for combi in combinations('12345', 3):
    pr += [''.join(combi)]
print(pr)
'''