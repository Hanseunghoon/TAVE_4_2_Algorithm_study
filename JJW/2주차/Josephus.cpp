#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;
queue<int>q;
 int main(){
 	int n, k; // n�� ����� �� �ο�, k��° ����� ����  
	cout << "����� �� �ο� ��:" ;
 	cin >> n;
 	cout << "k��° ������� :";
 	cin >> k;
 	//K��°�� �ƴ� ������� ,front ���� ���� �� �ٽ� �־� 
    for(int i = 0; i <= n; i++){
    	q.push(i); 
	}
    for(int i = 0; i < n-1; i++){
    	for (int j = 0; j < k -1 ; j++) {
            q.push(q.front());
            q.pop();
        }
        cout << q.front() << ", ";
        q.pop();

	}     
    cout << endl;
 	return 0; 
 }
 //front�� k�� �����°�� �ƴ� ���, pop(����)�� �� push(�� �ڷ� ������)�� �Ѵ�.
 //k�� �����°�� ���, pop(����)�ϸ� ����Ѵ�.
 //queue�� ������ �ɶ����� 1-2 ���� �ݺ��Ͽ� �����Ѵ�.
