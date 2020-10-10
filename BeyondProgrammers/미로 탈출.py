import sys
from collections import deque


def maze_escape():
    # 입력부
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    for i in range(N):
        maze += list(map(str, sys.stdin.readline().split()))

    # 이동 방향, 방문
    dirR = [0, 1, 0, -1]
    dirC = [1, 0, -1, 0]
    cntList = []
    visit = [[False for col in range(M)] for row in range(N)]
    visit[0][0] = True

    # dfs 구현... 이제 생각해보니 bfs로 해야 할 것 같은데
    def dfs(r, c, cnt, visited):
        # 큐 구현
        queue = deque()
        for i in range(4):
            if r + dirR[i] >= 0 and r + dirR[i] < N and c + dirC[i] >= 0 and c + dirC[i] < M and maze[r + dirR[i]][c + dirC[i]] == '1' and visited[r + dirR[i]][c + dirC[i]] == False:
                queue.append((r + dirR[i], c + dirC[i], cnt))

        # 큐가 빌 때까지
        while queue:
            NowR, NowC, NowCnt = queue.popleft()
            # 네 개의 방향
            visited[NowR][NowC] = True
            NowCnt += 1
            if NowR == N - 1 and NowC == M - 1:
                cntList.append(NowCnt)
                visited[NowR][NowC] = False
            else:
                bfs(NowR, NowC, NowCnt, visited)
                visited[NowR][NowC] = False


    # 함수 호출
    dfs(0, 0, 1, visit)
    print(min(cntList))


maze_escape()