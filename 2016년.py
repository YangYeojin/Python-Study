def solution(a, b):
    answer = ''
    added_days = 0
    day_of_the_week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    for i in range(a) :
        if i == 0 :
            added_days = 4      # 2015년 12월 31일이 목요일이기 때문
        elif i == 2:
            added_days += 29
        elif i in [1,3,5,7,8,10] :
            added_days += 31
        elif i in [4,6,9,11]:
            added_days += 30
    answer = day_of_the_week[(added_days+b) % 7]
    return answer