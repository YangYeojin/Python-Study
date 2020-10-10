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
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))

    # dfs 구현
    while queue:
        r, c = queue.popleft()

        if r == N - 1 and c == M - 1:
            print(visited[r][c])
            break

        for i in range(4):
            NowR = r + dirR[i]
            NowC = c + dirC[i]
            if 0 <= NowR < N and 0 <= NowC < M and maze[NowR][NowC] == '1' and visited[NowR][NowC] == False:
                visited[NowR][NowC] = visited[r][c] + 1
                queue.append((NowR, NowC))


maze_escape()

# bfs 이렇게 쓰는 거구나... 이제 dfs 말고 bfs도 쓸 수 있다!