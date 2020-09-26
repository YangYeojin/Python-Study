# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수 (스테이지를 깬 플레이어 포함 X)
# N : 전체 스테이지 개수    stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# 결과값 : 실패율이 높은 스테이지부터 그 스테이지 번호를 내림차순 배열로 return
# 제한사항 : 1 <= n <= 500, 1 <= len(stages) <= 200,000, 스테이지 번호는 1부터 시작, N+1은 마지막 스테이지를 깬 사용자
# 실패율이 같은 스테이지는 작은 번호의 스테이지가 먼저, 스테이지에 도달한 유저가 없는 경우 실패율은 0

# 1. 스테이지의 개수만큼 for 문을 회전시키면서 각 문제당 스테이지에 도달한 사람과 클리어하지 못한 플레이어 수를 셈
# 2. 실패율을 구해 문제의 번호 수와 함께 2차원 배열에 넣음
# 3. 실패율을 기준으로 reverse 하여 정렬함
# 4. 2차원 배열을 풀어 문제의 번호만 추출하여 리스트 형식으로 return 함

def solution(N, stages):
    answer = []
    i_and_failRate = []

    for i in range(1, N+1):
        if len(stages) == 0:
            i_and_failRate.append([i, 0])
        else:
            stages_bigger_then_i = list(filter(lambda x: x > i, stages))
            i_and_failRate.append([i, (len(stages) - len(stages_bigger_then_i))/len(stages)])
            stages = stages_bigger_then_i

    i_and_failRate = sum(sorted(i_and_failRate, key=lambda x: x[1], reverse=True), [])
    answer = i_and_failRate[0::2]
    return answer

# 문제점 : 시간이 너무 오래 걸림
# 테스트 22의 실행 결과 : 7191.93ms, 160MB
