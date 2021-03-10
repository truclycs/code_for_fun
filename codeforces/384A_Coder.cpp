#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cout << (n * n + 1) / 2 << "\n";
    bool flag = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (flag) {
                (j % 2) ? cout << "." : cout << "C";
            }
            else {
                !(j % 2) ? cout << "." : cout << "C";
            }
        }
        cout << "\n";
        flag = !flag;
    }
    return 0;
}