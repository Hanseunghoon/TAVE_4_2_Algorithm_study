#include<iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		int arr1[41] = { 0, };
		int arr2[41] = { 0, };
		arr1[0] = 1; arr1[1] = 0;
		arr2[0] = 0; arr2[1] = 1;
		for (int i = 2; i <= n; i++) {
			arr1[i] = arr1[i - 1] + arr1[i - 2];
			arr2[i] = arr2[i - 1] + arr2[i - 2];
		}
		cout << arr1[n] << " " << arr2[n] << endl;
	}
}