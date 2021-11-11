#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> l(n), r(n);
    for (int i = 0; i < n; i++) {
        cin >> l[i] >> r[i];
    }

    int min_left = l[0];
    int max_right = r[0];
    for (int i = 1; i < n; i++)  {
        min_left = min(min_left, l[i]);
        max_right = max(max_right, r[i]);
    }

    int res = -1;
    for (int i = 0; i < n; i++) {
        if (l[i] == min_left && r[i] == max_right) {
            res = i + 1;
            break;
        }
    }

    cout << res;
        
    return 0;
}