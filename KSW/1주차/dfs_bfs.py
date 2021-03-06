# 우선 본인은 컴공 출신이 아니며, 해당사항에 대한 용어를 거의 모른다. 이제 갓난아기이다.
# DFS와 BFS 문제를 한번 보자. 해당링크: https://www.acmicpc.net/problem/1260
# 그래프를 DFS로 탐색한 결과를 출력하는 프로그램을 작성하시오, 정답률 30퍼센트, 단 방문할 수 있는 정점이 여러 개인 경우,
# 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점번호는 1번부터 N번까지
# !입력 첫째 줄에 정점의 갯수 N(1보다 크거나 같고 1000보다 작거나 같다), 간선의 갯수 M(1보다 크거나 같고 1000보다 작거나 같다)
# 탐색을 시작할 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선의 방향은 같다.
# !출력은 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력한다.

# 용어: DFS는 깊이우선탐색(Depth First Search)이고 BFS는 너비우선탐색(Breadth First Search)를 의미한다.
