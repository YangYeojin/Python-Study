def solution(arr):
    # answer list를 선언한다.
    answer = []
    # answer list의 첫번째 값으로 arr 첫번째 값을 추가한다.
    answer.append(arr[0])
    # arr list의 요소 개수보다 1 작은 값만큼 반복하며
    for i in range(len(arr)-1):
        # arr list의 i+1번째 요소와 i번째 요소가 같지 않을 때
        if arr[i+1] != arr[i]:
            # answer list의 마지막에 i+1번째 요소를 추가한다.
            answer.append(arr[i+1])
    return answer