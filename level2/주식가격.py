'''
def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = 0
        if prices[i] == min(prices[i:]):
            temp = len(prices[i:]) - 1
        else:
            for j in range(len(prices[i+1:])):
                if prices[i] > prices[i+j]:
                    temp = j
                    break
            if temp == 0:
                temp = len(prices[i:]) - 1

        answer.append(temp)
    return answer
# 시간초과
'''


# dic으로 만들어서
# dic_list = [(pri, i) for i, pri in enumerate(prices)]
import operator
def solution(prices):
    dic_list = sorted([[i, pri] for i, pri in enumerate(prices)], key=operator.itemgetter(1))
    for i in range(len(dic_list)):
        # 가장 마지막에 기록된 주식 처리
        if dic_list[i][0] == len(dic_list)-1:
            dic_list[i].append(0)
        # 주식가격이 끝까지 떨어지지 않았을 때 처리
        elif dic_list[i][0] == min(dic_list[i:][0]):
            dic_list[i].append(len(dic_list[i:])-1)

        else:
            print(min(dic_list[i:][0]))
            dic_list[i].append("Q. 여기 어떻게 쓰면 될까요?")

        print(dic_list[i], "\t", dic_list[i+1:])
    print("\n", sorted(dic_list, key=operator.itemgetter(0)))
    return sum(sorted(dic_list, key=operator.itemgetter(0)), [])[2::3]


print("\n", solution([1, 4, 3, 2, 3, 2]))
print("\n=========================\n")
print("\n", solution([1, 2, 3, 2, 3]))