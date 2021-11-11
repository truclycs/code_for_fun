#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l = 0;
    vector<int> d(100001);
    int cnt = 0;
    int res = 0;
    for (int r = 0; r < n; r++) {
        d[a[r]]++;
        if (d[a[r]] == 1) {
            cnt++;
            if (cnt > 2) {
                while (true) {
                    d[a[l]]--;
                    if (d[a[l]] == 0) {
                        l++;
                        break;
                    }
                    l++;
                }
                cnt--;
            }
        }
        res = max(res, r - l + 1);
    }

    cout << res;
    return 0;
}