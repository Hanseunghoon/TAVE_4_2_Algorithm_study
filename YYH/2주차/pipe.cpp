#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(void){
	int count=0;
	stack <string> pip;
	string input;

	cin>>input;

	string c;
	
	for (int i=0; i<input.length(); i++)
	{
		c =input.substr(i, 1);//string을 하나씩 잘라 stack에 넣는다. 
		if(c=="(")
		{	pip.push(c);
			cout<<c<<"\n";
			cout<<count<<"\n";}
		else{
			c = pip.top();
			pip.pop();
			if (c=="(")
			{	count += pip.size();
			cout<<c<<"\n";
			cout<<count<<"\n";	}
			else	count++;
			cout<<c<<"\n";
			cout<<count<<"\n";
		}
		
	}
	cout<< count;
	return 0;
}

