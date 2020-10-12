import sys
import copy
from collections import deque


# 정점:N, 간선:M, 시작번호:V
N, M, V = map(int, sys.stdin.readline().split())

# 간선이 연결하는 두 정점의 번호 리스트
gr = list()
for _ in range(M):
    gr += [list(map(int, sys.stdin.readline().split()))]


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보가 담긴 그래프 생성
graph = [[] for i in range(N+1)]
visited = [True] * (N+1)
for i in gr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
    visited[i[0]] = False
    visited[i[1]] = False
for i in range(len(graph)):
    graph[i] = sorted(graph[i])




# 각 노드의 방문 정보를 1차원 리스트로 표현
visit = copy.deepcopy(visited)
dfs(graph, V, visit)
print()
visit = copy.deepcopy(visited)
bfs(graph, V, visit)
