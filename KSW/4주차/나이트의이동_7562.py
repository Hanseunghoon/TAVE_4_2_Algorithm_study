# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
# 입력: 첫째 줄에는 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 세 줄로 이루어져 있다.
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다.
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
# 출력: 각 테스트 케이스마다 나이트가 몇 번만에 이동할 수 있는지 출력한다.

# 접근법: bfs를 활용한다. 그림과 같이 초록색으로 표시된 나이트의 좌표를 구한다.

# deque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다.
from sys import stdin
from collections import deque

input = stdin.readline

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)
q = queue()

# 함수
def bfs():
    q.append((sx, sy))
    # 오른쪽에 값을 넣고 싶으면 append(), 왼쪽에서 값을 빼고 싶으면 popleft()를 사용
    while q:
        x, y = q.popleft()
        if x == ex and  y == ey:
            print(d[x][y])
            return

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not d[nx][ny]:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().splite())
    ex, ey = map(int, input().splite())
    d = [[0]*n for _ in range(n)]
    bfs()
