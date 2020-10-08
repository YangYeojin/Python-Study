import sys


def maze_escape():
    # 입력부
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    for i in range(N):
        maze += list(map(str, sys.stdin.readline().split()))
    visit = [[False for col in range(M)] for row in range(N)]
    roadLen = 1

    dirX = [1, 0, -1, 0]
    dirY = [0, 1, 0, -1]

    # dfs ~~ 이제 생각해보니 이건 bfs가 나았으려나?
    def dfs(graph, c, r, visited, cnt):
        visited[r][c] = True
        for k in range(4):
            if r == (N-1) and c == (M-1):
                print(cnt)
                break
            elif r+dirY[k] == N or c+dirX[k] == M:
                continue
            elif graph[r+dirY[k]][c+dirX[k]] == '1' and visited[r+dirY[k]][c+dirX[k]] is False:
                if k == 0 or k == 1:
                    cnt += 1
                    dfs(graph, c + dirX[k], r + dirY[k], visited, cnt)
                else:
                    cnt -= 1
                    dfs(graph, c+dirX[k], r+dirY[k], visited, cnt)

    # 함수 호출
    dfs(maze, 0, 0, visit, roadLen)


maze_escape()