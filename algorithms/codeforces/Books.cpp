#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, t;
    cin >> n >> t;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int res = 0;
    int l = 0;
    int sum_time = 0;
    for (int r = 0; r < n; r++) {
        sum_time += a[r];
        while (sum_time > t) {
            sum_time -= a[l];
            l++;
        }
        res = max(res, r - l + 1);
    }

    cout << res;

    return 0;
}