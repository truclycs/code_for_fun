#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, x, y;
    cin >> n >> m >> x >> y;
    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    vector<pair<int, int>> res;
    int i = 0;
    int j = 0;
    while (i < n && j < m) {
        if (a[i] - x <= b[j] && b[j] <= a[i] + y) {
            res.push_back(make_pair(i + 1, j + 1));
            i++;
            j++;
        }
        else if (b[j] <= a[i] - x) {
            j++;
        }
        else {
            i++;
        }
    }

    cout << res.size() << "\n";
    for (int i = 0; i < res.size(); i++) {
        cout << res[i].first << " " << res[i].second << "\n";
    }
    
    return 0;
}