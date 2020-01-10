#include <iostream>
#define MAX_SIZE 13
using namespace std;
int lotto[MAX_SIZE];
int combination[MAX_SIZE];
int k;

void DFS(int idx, int cnt){
	if(cnt==6){
		for(int i=0; i<6; i++){
			cout<<combination[i]<<" "; 
		}	
		cout<<"\n";
		return;
	}
	for(int i=idx; i<k; i++){
		combination[cnt] = lotto[i]; //조합에 숫자 넣는 중 
		DFS(i+1, cnt+1); //재귀로 다음 경우 호출   
	}
}  

int main (void){
	
	while(cin >>k && k){ //0을 입력할 때까지 받기 
		for(int i=0; i<k; i++){
			cin>>lotto[i];
		}
		DFS(0,0);//0부터 탐색 
		cout<<"\n";
	}	
	return 0;
}

