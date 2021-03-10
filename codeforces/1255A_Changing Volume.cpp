#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, a, b;
    cin >> t;
    while (t--) {
        cin >> a >> b;
        int x = abs(b - a);
        int x1 = x / 5;
        int res = x1;
        x -= x1 * 5;
        res += x / 2;
        x1 = x / 2;
        x -= x1 * 2;
        res+=x;
        cout << res << "\n";
    }
    return 0;
}