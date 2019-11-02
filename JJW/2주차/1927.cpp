#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
    priority_queue <int, vector<int>, greater<int> >q;
	//���� ���� ���� front�� �ֱ� ���� �켱 ���� ť ����
	//greater������ 
    int x ,n;
    cin >> n;
    
	for(int i = 0; i < n; i++){
        cin >> x;
        if (x == 0)
        {
            if (q.empty()) {
			 cout << '0'<< endl;
			}
            else{ 
				cout << q.top() << endl; 
				q.pop(); 
			}
        }
        else{
            q.push(x);
    	}
	}
    return 0;
}
/*1. ���� 0�϶�
  - ��������� 0���
  - ������� ������ q.pop
    2. ���� 0�� �ƴϸ� q.push*/


