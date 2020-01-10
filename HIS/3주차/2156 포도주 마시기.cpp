#include<iostream>
using namespace std;

int Max(int a, int b, int c) {
	if (a > b) {
		if (a > c) return a;
		else return c;
	}
	else {
		if (b > c) return b;
		else return c;
	}
}

int main() {
	int arr[10001] = { 0, };
	int ans[10001] = { 0, };
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	ans[0] = arr[0]; ans[1] = arr[0] + arr[1];
	ans[2] = Max(ans[1], arr[0] + arr[2], arr[1] + arr[2]);
	for (int i = 3; i < n; i++) {
		ans[i] = Max(ans[i - 3] + arr[i - 1] + arr[i], ans[i - 2] + arr[i], ans[i - 1]);
	}
	cout << ans[n - 1] << endl;
}