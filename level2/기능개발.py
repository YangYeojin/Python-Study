def solution(progresses, speeds):
    answer = []
    # while:문을 돌리면서 'progresses'의 각 요소에 'speeds'의 각 요소를 더해줌
    while len(progresses) > 0:
        progresses = [progresses+speeds for progresses, speeds in zip(progresses, speeds)]

        temp = 0    # 한 번에 배포되는 작업의 수를 알아내기 위한 변수
        # 리스트 'progresses'의 길이가 0 이상이고 현재 진행되고 있는 작업 중 가장 앞에 있는 기능의 진도가 100 이상일 때
        while len(progresses) > 0 and progresses[0] >= 100:
            # 가장 앞에 진행한 작업 및 진도율을 삭제하고 temp(오늘 배포할 수 있는 작업)에 1을 더해 줌
            progresses.pop(0)
            speeds.pop(0)
            temp += 1

        # 'temp'가 0 이상인 경우 (직전의 while:문에 한 번이라도 걸린 경우) 'temp'를 'answer'의 마지막 요소로서 추가해 줌
        if temp > 0:
            answer += [temp]
    return answer

print(solution([93,30,55], [1,30,5]))