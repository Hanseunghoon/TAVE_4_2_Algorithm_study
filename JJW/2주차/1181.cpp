#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
//�� ���� �ٲٱ� ���� ��� sort�Լ����� 3��° ���ڷ� �� ������ �� �Լ� ����
//bool �Լ��̸� (const ������& a, const ������& b){
      // return (a�� b���� �տ� �� ����);

bool compare(const string &a, const string &b) {
    //���̰� ���ٸ� ���� �� �������
    if (a.length() == b.length())
        return (a < b);
    //���̰� ���� �ʴٸ� ���̰� ���� 
    else
        return a.length() < b.length();

}

int main() {
	ios_base::sync_with_stdio(0);
    int test;
    cin >> test;
    string str[20000];
    for (int i = 0; i < test; i++) {
        cin >> str[i];
    }

    //3��° ���ڷ� Ư�� �� �Լ� 
    sort(str, str+test, compare);
    
    for (int i = 0; i < test; i++) {
        if (i != 0 && str[i] == str[i - 1]) 
			continue; //�տ� �ߺ��� �ܾ �ִٸ� continue�� ���ش� 
        else
        cout << str[i] << endl;    
    }

    return 0;

}
