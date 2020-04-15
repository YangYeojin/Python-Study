import itertools

def solution(numbers):
    answer = 0
    combined_list = []
    numbers_list = list(numbers)

    # 숫자 조합 만들기
    # map() : 리스트의 요소를 지정된 함수로 처리하는 함수
    # itertools.permutations() : 순열 구하는 함수
    temp = []
    for i in range(len(numbers_list)):
        temp = list(map(int, map("".join, itertools.permutations(numbers_list, i+1))))
        temp = list(temp)
        combined_list += temp
        combined_list = list(set(combined_list))
        print("combined_list : ", combined_list)

    zero_and_one = [0, 1]
    combined_list = list(set(combined_list) - set(zero_and_one))
    print("combined_list : ", combined_list)

    # 소수 찾기
    for i in range(len(combined_list)):
        # 2부터 나온 수의 제곱근까지 중에서 나누어 떨어지는 것이 없을 때 소수임을 확인할 수 있다.
        # 제곱근 구하는 공식 : x ** 0.5
        square_root_int = 0
        square_root_int = int(combined_list[i] ** 0.5)
        should_0 = 0
        for j in range(square_root_int):
            if j+1 != (1 or 2) and combined_list[i] % (j+1) == 0:
                should_0 += 1
        if should_0 == 0:
            answer += 1
    return answer
# 테스트 7 실패

print(solution("17"))
print(solution("011"))