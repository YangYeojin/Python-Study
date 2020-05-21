# 1. 점수 분리
#    for 3:문 돌리면서 '0'<dartResult[a+1]<'9' 이면 continue; (a는 지금 읽고 있는 자리수)
#    각 기회를 통해 얻은 점수는 [,,]로 분리한 후 마지막에 계산하면 좋을 듯
#    10점을 획득할 경우를 위해 if:로 조치를 취해 줌
# 2. 점수의 제곱 계산
#    score[i] **= Squ
# 3. 보너스 또는 차감 점수 계산

def solution(dartResult):
    answer = 0
    pre = 0
    now = 0
    a = 0   # 현재 읽고 있는 또는 이제 읽어야 할 'dartResult'의 자리수

    for i in range(3):
        # 사용자가 얻은 점수를 'now'에 넣고 다음 자리(제곱)를 읽기 위해 a에 적절한 값을 더해줌
        # 숫자를 읽고 있는 중 다음 자리가 숫자 0이면 현재 획득한 점수가 10인 경우밖에 없으므로 'now'에 10을 넣음
        if dartResult[a+1] == '0':
            now = 10
            a += 2
        else:
            now = int(dartResult[a])
            a += 1
        print('now', now)

        # 점수의 제곱 계산
        if dartResult[a] == 'S':
            now **= 1
        elif dartResult[a] == 'D':
            now **= 2
        elif dartResult[a] == 'T':
            now **= 3
        a += 1
        print('now after square', now)

        if len(dartResult) == a:
            answer += pre
            answer += now
            break
        elif dartResult[a] == '*':
            print(dartResult[a])
            answer += pre * 2
            pre = now * 2
            a += 1
        elif dartResult[a] == '#':
            print(dartResult[a])
            answer += pre
            pre = now * (-1)
            a += 1
        else:
            answer += pre
            pre = now

        if i == 2:
            answer += pre
        print('pre', pre, 'answer', answer)
        print(' ')
    return answer

print(solution('1D2S3T*'))
print('-'*20)
print(solution('1T2D3D#'))