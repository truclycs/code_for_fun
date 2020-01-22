#include <bits/stdc++.h>
using  namespace std;

int main() {
    int t, a, b, c, d, k;
    cin >> t;
    while (t--) {
        cin >> a >> b >> c >> d >> k;
        int x, y;
        x = (a - 1) / c + 1;
        y = (b - 1) / d + 1;
        if (x + y <= k) {
            cout << x << " " << y << '\n';
        }
        else {
            cout << -1 << "\n";
        }
    }
    return 0;
}