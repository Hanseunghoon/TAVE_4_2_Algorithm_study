#include <iostream>
#include <queue>

using namespace std;

int N, M, V; // ������ ���� , ������ ����, Ž���� ������ ������ ��ȣ  
int visit[1001]; //  �湮�ߴ� ��� üũ 
int A[1001][1001]; // ������� ���� �ޱ� ���� ���   �湮�� = 1 �̹湮 0 
int DFS(int V){
	cout << V << ' '; // ù start ���� ��ȣ ���
    visit[V] = 1; // �湮 �Ͽ����Ƿ� visit[start] = 1�� �湮 üũ
    for (int i = 1; i <= N; i++) // ������ ������� �ݺ����� ���鼭 �湮�� �߰ų� ������Ŀ� 0�� ������ ������                                                    ��, dfs(i) ���
    {
        if (visit[i] == 1 || A[V][i] == 0) 
		continue;
        DFS(i);
    }
    
}
int BFS(int V){
	queue<int> q;
	q.push(V); // ù queue�� �ִ� �� push
    visit[V] = 1; // ���� �湮 
      while (!q.empty()) { //queue�� �� ������ while��
       	V = q.front(); 
        cout << V << " ";
        q.pop();
        for (int i = 1; i <= N; i++)
        {
            if (A[V][i] ==1 && visit[i] == 1){
            	continue;
            	q.push(i);
            	visit[i] = 0;
        	}
        }
    }

}
int main(){
	ios_base::sync_with_stdio(0);
	int x,y; // x node, y node
	cin >> N >> M>> V; 
	for(int i = 0; i < M; i++){
		cin >> x >> y;
		A[x][y] = A[y][x] = 1; // ��������� ���� ���� ���Ƽ�  
	}
	cout << BFS(V) << endl;
	cout << DFS(V) << endl;
	
	return 0;
}
