#include <bits/stdc++.h>
using namespace std;

int main() {
    int q, n;
    cin >> q;
    while (q--) {
        cin >> n;
        if (n == 2) {
            cout << 2 << "\n";
        }
        else {
            cout << (n + 1) / 2 * 2 - n << "\n";
        }
    }
    return 0;
}