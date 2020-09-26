def solution(board):
    maxSquare = max(board[0][:])
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 0:
                continue
            else:
                if board[i-1][j] > 0 and board[i][j-1] > 0:
                    board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                if maxSquare < board[i][j]:
                    maxSquare = board[i][j]
    return maxSquare ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
print(solution([[1,0],[0,0]]))