#include <iostream>
using namespace std;


int count0, count1;
int fibonacci(int n) {
    if (n == 0) {
        count0 +=1;
    } else if (n == 1) {
        count1+=1;
    } else {
         fibonacci(n-1) + fibonacci(n-2);
    }
    
}

int main (void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n, t;
	cin>>t;
	for(int i =0; i<t; i++){
		cin>>n;
//		scanf("%d",&n);
		fibonacci(n);
		cout<<count0<<" "<<count1<<"\n";
//		printf("%d %d \n",count0,count1);
		count0=0, count1=0;		
	}	
}
