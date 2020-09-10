def bignum():
    answer = 0
    N, M, K = map(int, input("N, M, K를 띄워쓰기 하여 입력 : ").split())
    li = list(map(int, input("배열을 입력 : ").split()))

    li.sort(reverse=True)
    for i in range(M):
        if i % (K+1) != 0:
            answer += li[0]
        else:
            answer += li[1]
    return answer


print(bignum())