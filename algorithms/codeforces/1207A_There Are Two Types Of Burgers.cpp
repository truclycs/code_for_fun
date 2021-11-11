#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, b, p, f, h, c;
    cin >> t;
    while (t--) {
        cin >> b >> p >> f >> h >> c;
        if (h > c) {
            int x = min(p, b / 2);
            cout << h * x + c * min(f, (b - x * 2) / 2);
        }
        else {
            int x = min(f, b / 2);
            cout << h * min(p, (b - x * 2) / 2) + c * x;
        }
        cout << "\n";
    }
    return 0;
}
