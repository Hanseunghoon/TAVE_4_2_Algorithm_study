# 젤다의 전설 시리즈의 주인공, 링크는 지금 도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다. [0][0]번 칸이기도 하다.
# 왜 이런 곳에 들어왔냐고 묻는다면 밖에서 사람들이 자꾸 "젤다의 전설에 나오는 녹색 애가 젤다지?"라고 물어봤기 때문이다. 링크가 녹색 옷을 입은 주인공이고
# 젤다는 그냥 잡혀있는 공주인데, 게임 타이틀에 젤다가 나와있다고 자꾸 사람들이 이렇게 착각하니까 정신병에 걸릴 위기에 놓인 것이다.
# 하여튼 젤다...아니 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다. 동굴의 각 칸마다 도둑루피가 있는데,
# 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다. 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며,
# 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다. 링크가 잃을 수밖에 없는 최소 금액은 얼마일까?

# 입력: 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다.
# (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다. 이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가
# 공백으로 구분되어 차례대로 주어진다. 도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻이다. 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수다.

# 출력: 각 테스트 케이스마다 한 줄에 걸쳐 정답을 형식에 맞춰서 출력한다. 형식은 예제 출력을 참고하시오.

# 접근법: 링크가 검은 루피를 먹으면서 루피를 잃으면서 이동할 때, 가장 적게 잃는 경로를 구하는 문제다.
# 각 칸마다 잃을 수 있는 루피는 0~9 이므로, 다익스트라 알고리즘을 통해 구현하면 된다.
# M * N 맵 입력, dist 이용 / dist[-1][-1] 이 값에 루피인 a[0][0]을 더해줘야함 / 테스트케이스마다 dist배열 초기화

# heapq가져오기
from heapq import heappop, heappush
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

t = 0
INF = 1e9
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# 다익스트라 함수만들기
def Dijkstra(n, a, dist):
    pd = []
    heappush(pd, (0, 0, 0, 0))
    dist[0][0] = 0

    while pd:
        d, x, y = heappop(pd)

        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            nd = d + a[nx][ny]
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heappush(pd, (nd, nx, ny))

    return dist[n-1][n-1] + a[0][0]

while True:
    t += 1
    n = int(input())

    if n is 0:
        break
    a = [list(map(int, input().splite())) for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]
    print("Problem %d: %d\n" % (t, dijkstra(n, a, dist))
