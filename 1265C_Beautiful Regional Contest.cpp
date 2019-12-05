#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        int m = 0;
        int b[n];
        b[0] = 1;
        for (int i = 1; i < n; i++) {
            if (a[i] == a[i - 1]) {
                b[m]++;
            }
            else {
                m++;
                b[m] = 1;
            }
        }

        int x, y, z;
        x = b[0];
        y = 0;
        z = 0;
        for (int i = 1; i <= m; i++) {
            if (y <= x) {
                y += b[i];
            }
            else if (z <= x || (x + y + z + b[i]) <= n / 2) {
                z += b[i];
            }
        }

        if (x + y + z <= n / 2 && x > 0 && y > 0 & x > 0) {
            cout << x << " " << y << " " << z << "\n";
        }
        else {
            cout << "0 0 0\n";
        }
    }

    return 0;
}