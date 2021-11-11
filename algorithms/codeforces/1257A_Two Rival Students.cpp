#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n, x, a, b;
    cin >> t;
    while (t--) {
        cin >> n >> x >> a >> b;
        if (a > b) {
            swap(a, b);
        }

        int da = max(1, a - x);
        int db = min(b + x, n);
        int xa = x - (a - da);
        int xb = x - (db - b);

        cout <<  max(b - da + min(xa, n - b), db - a + min(xb, a - 1)) << "\n";
    }
    return 0;
}