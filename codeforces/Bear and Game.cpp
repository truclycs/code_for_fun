#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n, x;
    vector<int> a;
    cin >> n;
    a.push_back(0);
    for (int i = 0; i < n; i++) {
        cin >> x;
        a.push_back(x);
    }

    int res = 0;
    for (int i = 0; i <= n; i++) {
        if (a[i] - a[i - 1] > 15) {
            break;
        }
        else {
            res = a[i];
        }   
    }

    cout << min(res + 15, 90);
    return 0;
}