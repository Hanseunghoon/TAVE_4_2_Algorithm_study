#include <iostream>
#include <queue>
using namespace std;

int main(void){
	
	queue<int> q;
	int n,k;
	int count=0;
	int c=0;
	cin>>n>>k;
	if(k>n ||n>5000 ||k<0)
		return -1;
	
	for (int i=1;i<=n; i++){
		q.push(i);
	}
	while(!q.empty()){
	
		count++;
		if(count%k==0)
		{
			cout<<q.front();
			q.pop();
				}
		else{
		
		c=q.front();
		q.pop();
		q.push(c);
		}
	}
}
