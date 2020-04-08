def solution(s):
    answer = True
    a = list(s)
    if len(a) == 4 or len(a) == 6:
        answer = s.isdigit()
    else :
        answer = False
    return answer

#print(solution("123456"))      #True
#print(solution("123df6"))      #False
#print(solution("123f6eee"))    #False
#print(solution("12345678"))    #False
#print(solution("123"))         #False
#print(solution("12d"))         #False