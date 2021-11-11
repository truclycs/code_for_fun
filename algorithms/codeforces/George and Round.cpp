#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    int cnt = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j < m && b[j] < a[i]) {
            j++;
        }
        if (j < m) {
            cnt++;
            j++;
        }
    }

    cout << n - cnt;
    return 0;
}