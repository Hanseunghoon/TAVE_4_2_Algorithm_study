#include <iostream>
using namespace std;
int sugar (int n);

int main (void){
	ios_base::sync_with_stdio(0);


	int n;
	
	cin>>n;
	if(n<3 ||n>5000)
	return -1;
	
	cout<<sugar(n)<<"\n";
	
	}

int sugar (int n){
	
	int origin = n;
	int five=0; //5kg�� ���� ������ ���� 

	if (n<5) { //5kg�� ������ �� ���� ��� 
		if(n==3) return 1;	 
		else return -1;
	}
	if(n%5==0)
		return n/5; 

	if(n>5){ //5kg�� ���� ������ �� �ִ��� ������ �Ǻ� 
		
		while((n-5)>0){				
			n -= 5;
			five++;
			
			if(n%3==0 && n<=5){ //5kg�� �������� �������� 3�� ����� ��� �� 
				return	five + (n/3);
				}

			if(n%3 !=0 && n<=5){ //�������� ����� 3�� �ƴ� �� 5�� �ѹ� ���� 3�� ����� �Ǵ� �� Ȯ�� 
				n += 5;
				if(n%3==0)
					return	(five-1) + (n/3);	
				if(origin %3 ==0) //5�� ������ 5kg�� ������ �� ���� ��� 
					return n/3;		
				}	
			 

		}
			
	}
}
