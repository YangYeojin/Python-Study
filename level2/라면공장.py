# idea 1
# 한 번에 많은 양을 공급받을 수 있으면 좋음
# -> 많은 양을 stock 범위 안에서 가장 많은 밀가루를 공급해주는 날짜에 밀가루 공급받기
# k - (현재까지의 날짜) <= stock 이면 answer 반환하기

import heapq
'''
def solution(stock, dates, supplies, k):
    answer = 0
    day = 0
    temp = []
    for i in range(k):
        # i 날짜에 들어올 수 있는 공급을 'temp'에 담음
        if i <= dates[-1] and dates[day] == i:
            heapq.heappush(temp, -supplies[day])
            day += 1
        # 재고가 0일 때 'temp'에 저장된 공급 가능 수량 중에서 가장 많은 수량을 공급받음
        if stock == 0:
            stock += -heapq.heappop(temp)
            answer += 1
        stock -= 1
    return answer
### 효율성 3번에서 걸림
'''
'''
def solution(stock, dates, supplies, k):
    answer = 0
    day = 0
    temp = []
    for i in range(k):
        # i 날짜에 들어올 수 있는 공급을 'temp'에 담음
        if i <= dates[-1]:
            if dates[day] == i:
                heapq.heappush(temp, -supplies[day])
                day += 1
            # 재고가 0일 때 'temp'에 저장된 공급 가능 수량 중에서 가장 많은 수량을 공급받음
            if stock == 0:
                stock += -heapq.heappop(temp)
                answer += 1
            stock -= 1
        else:
            while True:
                if stock >= k-i:
                    return answer
                else:
                    stock += -heapq.heappop(temp)
                    answer += 1
    return answer
### 효율성 2,3번에서 걸림
'''


print(solution(4, [4,10,15],[20,5,10],40))
print(solution(4, [4,7,10,15,21,22,25],[20,7,5,10,1,5,2],40))