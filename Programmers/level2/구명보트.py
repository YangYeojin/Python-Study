from collections import deque
'''
def solution(people, limit):
    answer = 0
    boat = people.pop()
    for i in range(len(people)-1, 0, -1):
        while boat > 0 and boat + people[i] <= limit:
            boat += people.pop()
    return answer
'''
'''
# 구명보트 최대 인원이 2명인 것을 고려하지 않았음
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while len(people) > 0:
        boat = people.pop(0)
        temp = 0
        for i in range(len(people)):
            if boat > 0 and boat + people[i - temp] <= limit:
                boat += people.pop(i-temp)
                temp += 1
            if len(people) > 0 and boat + people[-1] > limit:
                break
        answer += 1
    return answer
'''


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    print(people)
    while len(people) > 0:
        if len(people) == 1:
            people.pop()
            answer += 1
            print(people, answer)
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
            print(people, answer)
        else:
            people.popleft()
            answer += 1
            print(people, answer)
    return answer


print(solution([60, 40, 50, 80, 45, 50], 100))
print(solution([70, 50, 80, 50], 100))