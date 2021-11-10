#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);
    int res = 0;
    for (int i = 1; i < n; i++) {
        res += a[i] - a[i - 1] - 1;
    }
    cout << res;
    return 0;
}