#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, x;
    cin >> n >> x;
    vector<long long> c(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }

    sort(c.begin(), c.end());

    long long res = 0;
    for (int i = 0; i < n; i++) {
        res += c[i] * max(1LL*1, x--);
    }

    cout << res;
    return 0;
}