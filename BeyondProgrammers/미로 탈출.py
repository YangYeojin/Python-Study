import sys


def maze_escape():
    # 입력부
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    for i in range(N):
        maze += list(map(str, sys.stdin.readline().split()))
    roadLen = 1

    # range 오류 귀찮으니까 그냥 0으로 패딩
    pMaze = []
    for i in range(N+2):
        if i == 0 or i == N+1:
            pMaze += ['0'*(M+2)]
        else:
            pMaze += ['0'+maze[i-1]+'0']
    visit = [[False for col in range(M+2)] for row in range(N+2)]   # 방문 여부 확인하는 테이블도 패딩한 크기로 그림

    # 이동 방향
    dirX = [0, 1, -1, 0]
    dirY = [1, 0, 0, -1]

    # dfs ~~ 이제 생각해보니 이건 bfs가 나았으려나?
    def dfs(graph, c, r, visited, cnt):
        visited[r][c] = True
        for k in range(4):
            if r == N and c == M:
                print(cnt)
                break
            elif graph[r+dirY[k]][c+dirX[k]] == '1' and visited[r+dirY[k]][c+dirX[k]] is False:
                cnt += 1
                dfs(graph, c + dirX[k], r + dirY[k], visited, cnt)
                if r == N and c == M:
                    print(cnt)
                    break
                else:
                    cnt -= 1

    # 함수 호출
    dfs(pMaze, 1, 1, visit, roadLen)


maze_escape()