# 우선 본인은 컴공 출신이 아니며, 해당사항에 대한 용어를 거의 모른다. 이제 갓난아기이다.
# DFS와 BFS 문제를 한번 보자. 해당링크: https://www.acmicpc.net/problem/1260
# 그래프를 DFS로 탐색한 결과를 출력하는 프로그램을 작성하시오, 정답률 30퍼센트, 단 방문할 수 있는 정점이 여러 개인 경우,
# 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점번호는 1번부터 N번까지
# !입력 첫째 줄에 정점의 갯수 N(1보다 크거나 같고 1000보다 작거나 같다), 간선의 갯수 M(1보다 크거나 같고 1000보다 작거나 같다)
# 탐색을 시작할 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선의 방향은 같다.
# !출력은 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력한다.

# 용어: DFS는 깊이우선탐색(Depth First Search)이고 BFS는 너비우선탐색(Breadth First Search)를 의미한다.
# 접근법: ㄷ셔너리에 간선들을 토대로 연결된 노드들을 표시한다. 노드들은 집합 자료형을 이용하였다. dfs 탐색을 한다.

dic = {}

def setdic(m):
    for _ in range(0, m):
        node_A, node_B = map(int, input().splite())
        if not node_A in dic:
            dic[node_A] = set([])
        if not node_B in dic:
            dif[node_B] = set([])

        dic[node_A].add(node_A)
        dic[node_B].add(node_B)

# 방문했던 노드를 기억하는 배열 visited 와 현재 노드들이 쌓여있는 스택 temp 를 만든다.
def bfs(s):
    if not s in dic:
        print(s)
        return

    visited = []
    temp = [s]
    while temp :
        n = temp.pop(0) # 큐 출력
        if not n in visited : # 순회하면서 방문하지 않은 노드의 자식 노드들을 스택에 쌓는다. 자식노드들을 쌓을 때 현재 방문했던 노드와 차집합하여 또 방문하는 일이 없도록 한다.
            visited.append(n) # 자료 입력
            temp.extend(sorted(list(dic[n] - set(visited)))) # set 자료형은 순서를 보장하지 않기 때문에 정렬을 해주면서 쌓는다.
    visited = list(map(str, visited))  # 방문하지 않은 노드는 set를 이용하면 쉽게 구현가능
    print(" ".join(visited))


def dfs(s):
    if not s in dic :
        print(s)
        return
    visited = []
    temp = [s]
    while temp :
        n = temp.pop()
        if not n in visited :
            visited.append(n)
            temp.extend(sorted(list(dic[n] - set(visited)), reverse=True)) # 작은 노드부터 탐색하기 위해 sorted 에 reverse 옵션을 사용
    visited = list(map(str, visited))
    print(" ".join(visited))


def main () :
    n, m, v = map(int, input().split())
    setdic(m)
    dfs(v)
    bfs(v)

main()


# 시간을 단축
'''
from collections import deque

graph = {}

n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

print(DFS(graph, start))
print(BFS(graph, start))
'''
