'''
def solution(s):
    answer = list()

    def divide_list(l, n):
        for x in range(0, len(l), n):
            yield l[x:x + n]

    for i in range(1, int(len(s) * 1/2) + 1):
        cnt, more2cnt = 0, 0
        li = list(divide_list(s, i))
        for j in range(1, len(li)):
            if li[j] == li[j-1]:
                cnt += 1
                if j >= 2 and li[j] == li[j-2]:
                    more2cnt += 1
        answer += [len(s)-cnt*i + cnt - more2cnt]
    return min(answer)
'''

import re

def solution(s):
    answer = list()

    def divide_list(l, n):
        for x in range(0, len(l), n):
            yield l[x:x + n]

    for i in range(1, int(len(s) * 1/2) + 2):
        li = list(divide_list(s, i))
        new = str(li[0])
        for j in range(1, len(li)):
            if li[j] != li[j-1]:
                new += li[j]
            else:
                if new[-1].isdigit():
                    temp = ''.join(re.findall("\d+$", new))
                    new = new[:-len(temp)]
                    new += str(int(temp) + 1)
                else:
                    new += '2'
        temp = 0
        for k in new:
            temp += 1
        answer += [temp]
    return min(answer)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("xababcdcdababcdcd"))
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))