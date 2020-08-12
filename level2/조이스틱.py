def solution(name):
    answer = 0
    made = list('A'*len(name))
    name = list(name)
    A, Z = ord('A'), ord('Z')
    idx = 0
    notA = [i for i, value in enumerate(name) if value != 'A']

    while name != made:
        # 현재 위치의 알파벳 변경
        alphabet = ord(name[idx])
        made[idx] = name[idx]
        if alphabet - A <= Z - alphabet + 1:
            answer += alphabet - A
        else:
            answer += Z - alphabet + 1
        if len(notA) == 1:
            break
        elif name[idx] != 'A':
            idxNotA = notA.index(idx)
            del notA[idxNotA]

        # 다음에 변경할 알파벳의 위치 찾기
        if name != made:
            tmp = list(map(lambda x: x - idx, notA)) + list(map(lambda x: x + len(name[idx:]) - 1 - idx, notA))
            #tmp = list(map(lambda x: -x if x < 0 else x, tmp))
            idxR = min(tmp) #list(filter(lambda x: x > idx, tmp))[0]
            if idxR < 0:
                idxR = max(tmp)
            tmp = list(map(lambda x: len(name) - idx + x - 1, notA)) + list(map(lambda x: len(name) - x + idx, notA))
            idxL = min(tmp)
            if idxR <= idxL:
                answer += idxR
                if idxR > len(name):
                    idx = idxR - len(name)
                else:
                    idx = idxR + idx
            else:
                answer += idxL
                if idxL > len(name[:idx]):
                    idx = len(name) - (len(name[:idx]) - idxL) - 2
                else:
                    idx = idxL
    return answer


#print(solution("JEROEN")) ## 56
#print(solution("JAAAN")) ## 23
#print(solution("ABAAAAAAAAABB")) ## 7
print(solution("ABAAABAAAAABB"))

'''
def solution(name):
    answer = 0
    sliding = 0
    A = ord('A')
    Z = ord('Z')
    NoLeft = True

    for i in range(len(name)):
        alphabet = ord(name[i])
        if alphabet - A <= Z - alphabet + 1:
            answer += alphabet - A
        else:
            answer += Z - alphabet + 1

        sliding += 1
        if alphabet != A:
            answer += sliding
            sliding = 0

        if NoLeft == True and i != 0:
            if alphabet == 65:
                answer -= 1
            else:
                NoLeft = False
    return answer - 1
'''