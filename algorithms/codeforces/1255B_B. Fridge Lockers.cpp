#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n, m;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a, a + n);

        if (m < n || n == 2) {
            cout << -1 << "\n";
            continue;
        }

        int sum = a[0] + a[n - 1];
        for (int i = 1; i < n; i++) {
            sum += a[i] + a[i - 1];
        }

        sum += (m - n) * (a[0] + a[1]);
        cout << sum << "\n";

        for (int i = 1; i < n; i++) {
            cout << i << " " << i + 1 << "\n";
        }
        cout << 1 << " " << n << "\n";
        for(int i = 0 ; i < m - n; i++) {
            cout << "1 2\n";
        }
    }
    return 0;
}