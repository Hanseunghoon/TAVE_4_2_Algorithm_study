# 그림과 같은 정사각형 모양의 지도가 있다. 1은 집이 있는 곳, 0은 집이 없는 곳이다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 그림2는 그림1 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
# 입력: 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
# 출력: 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

# 접근법: DFS, BFS 완전탐색으로 풀 수 있는 문제이다. 단지는 서로 이어져 있으며, 인접한 집이 있는지 DFS로 탐색, 탐색하면서 집의 수를 세고 값을 0으로 변경
# 0은 집이 없거나 이미 방문한 노드이므로 다시 방문 하지 말자, 탐색이 끝나면 단지는 모두 0으로 되어 있다.
# 맵 처음부터 끝까지 탐색하면서 아직 방문하지 않은 곳이 있다면, DFS로 다시 탐색한다. dfs를 처음 시작한 횟수가 단지의 수, 각 단지내 집의 수 오름차순 정렬

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
m = [list(sys.stdin.readline()) for _ in range(n)]

count = 0
apts = []

def bfs(x, y):
    global count
    m[x][y] = '0'
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)

for i in range(n):
    for j in range():
        if m[i][j] == '1':
            count = 0
            dfs(i, j)
            apts.append(count)

print(len(apts))
apts.sort()

for i in apts:
    print(i)
