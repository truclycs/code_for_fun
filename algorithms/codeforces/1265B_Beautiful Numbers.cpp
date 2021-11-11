#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        pair<int, int> a[n];
        int pos;
        for (int i = 0; i < n; i++) {
            cin >> a[i].first;
            a[i].second = i;
        }

        sort(a, a + n);

        pair<int, int> v[n];
        v[0].first = a[0].second;
        v[0].second = a[0].second;
        for (int i = 1; i < n; i++) {
            v[i].first = max(v[i - 1].first, a[i].second);
            v[i].second = min(v[i - 1].second, a[i].second);
        }
        for (int i = 0; i < n; i++) {
            if (abs(v[i].first - v[i].second) == i) {
                cout << 1;
            }
            else {
                cout << 0;
            }
        }

        cout << "\n";
    }
    return 0;
}