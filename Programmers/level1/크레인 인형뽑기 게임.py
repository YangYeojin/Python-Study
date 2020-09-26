def solution(board, moves):
    answer = 0
    basket = []

    for x in board:
        for y in x:
            print(y, end=" ")
        print()
    print("")

    for i in range(len(moves)):
        print("========= ", i+1, "번째 =========")
        column = int(moves[i]) -1
        print("column : ", moves[i])
        j = 0

        if board[-1][column] != 0:
            while board[j][column] == 0:
                j += 1
            doll = board[j][column]
            board[j][column] = 0
            print("doll : ", doll)
            # 바구니의 두 인형이 같으면 사라지는 파트
            if len(basket) >= 2 and basket[-1] == doll:
                del basket[-1]
                answer += 2
            else :
                basket.append(doll)

        print("basket : ", basket)
        for x in board:
            for y in x:
                print(y, end=" ")
            print()
        print("")
    return answer



a = [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]

print("result : ", solution(a, b))



'''
def solution(board, moves):
    answer = 0
    basket = []

    for i in range(len(moves)):
        column = int(moves[i]) -1
        j = 0

        if board[-1][column] != 0:
            while board[j][column] == 0:
                j += 1
            doll = board[j][column]
            board[j][column] = 0
            if len(basket) >= 1 and basket[-1] == doll:
                del basket[-1]
                answer += 2
            else :
                basket.append(doll)
    return answer
'''