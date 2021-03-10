#include <bits/stdc++.h>
using namespace std;

int main() {
    int s, n;
    cin >> s >> n;
    pair<int, int> x[n];
    for (int i = 0; i < n; i++) {
        cin >> x[i].first >> x[i].second;
    }

    sort(x, x + n);

    for (int i = 0; i < n; i++) {
        if (x[i].first >= s) {
            cout << "NO";
            return 0;
        }
        s += x[i].second;
    }

    cout << "YES";
    return 0;
}
