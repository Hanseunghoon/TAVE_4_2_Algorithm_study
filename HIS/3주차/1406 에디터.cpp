#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<char> v1;
vector<char> v2;

int main() {
	string def = "";
	int n = 0;
	char cmd;
	char cmd2;

	cin >> def;
	for (int i = 0; i < def.size(); i++)
		v1.push_back(def[i]);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == 'P') {
			cin >> cmd2;
			v1.push_back(cmd2);
		}
		else if (cmd == 'L') {
			if (!v1.empty()) {
				char _tmp = v1.back();
				v1.pop_back();
				v2.push_back(_tmp);
			}
		}
		else if (cmd == 'D') {
			if (!v2.empty()) {
				char _tmp = v2.back();
				v2.pop_back();
				v1.push_back(_tmp);
			}
		}
		else if (cmd == 'B') {
			if (!v1.empty()) {
				v1.pop_back();
			}
		}
	}
	for (int i = 0; i < v1.size(); i++)
		cout << v1[i];
	for (int i = 0; i < v2.size(); i++)
		cout << v2[v2.size() - i - 1];
}

/*
L : 커서를 왼쪽으로 한칸 옮김
D : 커서를 오른쪽으로 한칸 옮김
B : 커서 왼쪽에 있는 문자 삭제
P X : X라는 문자를 커서 왼쪽에 추가함

첫째줄에 초기 문자열 주어짐 (길이 < 100,000 )
명령어 개수
*/

/*
vector		커서	vector
aaaa		|		 bbbb
시작  끝			끝  시작
*/