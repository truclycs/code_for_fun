#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a, a + n);

    int res = 0;
    for (int i = 0; i < m; i++) {
        if (a[i] < 0) {
            res += a[i];
        }
        else {
            break;
        }
    }

    cout << abs(res);
    return 0;
}