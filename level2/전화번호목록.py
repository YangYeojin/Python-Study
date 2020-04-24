# 문제 파악 : 원소가 문자열로 된 리스트를 정렬하여 어느 한 원소가 다른 원소의 (가장 앞의)일부인 경우가 있을 때 false를 반환함
def solution(phone_book):
    answer = True
    # 1. list 정렬
    phone_book = sorted(phone_book)
    # 2. 모든 번호를 다음 번호와 비교함
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer

print(solution(["119", "97674223", "1195524421"]))