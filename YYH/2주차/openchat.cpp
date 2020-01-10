#include <string>
#include <utility>
#include <vector>
#include <iostream>
using namespace std;
vector<string> solution(vector<string> record);
int main (void){
	
	string enter[3] = {"enter","leave","change"};
	
	string state, uid , nickname;
	
	

	vector< pair<string, string> >  vec1;
	vector<string> record;
	string samp;


		int j=0;
		cin >> state>> uid>> nickname;
		
		for(int i=0; i<vec1.size()-1; i++) 
			if(vec1[i].first == uid)
			j++;
		
		if(state==enter[0])
		{
			vec1.push_back(make_pair(uid, nickname));
			samp = "\"" +vec1[j].second+"´ÔÀÌ µé¾î¿Ô½À´Ï´Ù\"";
			record.push_back(samp);
			  
		}
		if(state == enter[1])
		{
			samp ="\"" + vec1[j].second +"´ÔÀÌ ³ª°¬½À´Ï´Ù\"";
			record.push_back(samp);
		}
		if(state==enter[2])
		{		
			vec1[j].second=nickname;
		} 
	
	
	solution(record);
	 
}


vector<string> solution(vector<string> record) {
    vector<string> answer = record;
    return answer;
    
}
