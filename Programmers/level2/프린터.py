# 1. while:문으로 프린터 계속 작동
#    'answer'은 출력된 문서의 수를 표시할 것
# 2. if 대기목록 가장 앞에 있는 문서의 숫자가 가장 클 때: 가장 앞 문서를 pop & location-1 & answer + 1
#       if 'location'이 0이면 answer 출력
# 3. else: 가장 앞 문서를 마지막으로 이동(pop&append) & location-1
def solution(priorities, location):
    answer = 0
    print("start\t", priorities, "\tanswer", answer, "\tlocation", location)
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            location -= 1
            answer += 1
            if location == -1:
                return answer
            else:
                print("if\t\t", priorities, "\tanswer", answer, "\tlocation", location)
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            location -= 1
            if location == -1:
                location = len(priorities)-1
            print("else\t", priorities, "\tanswer", answer, "\tlocation", location)
    return answer


print(solution([2, 1, 3, 2], 2))
print("\n")
print(solution([1, 1, 9, 1, 1, 1], 0))