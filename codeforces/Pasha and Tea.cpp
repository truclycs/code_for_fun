#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    double w;
    cin >> n >> w;
    vector<double> a(n * 2);
    for (int i = 0; i < 2 * n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    double x = min(a[0], a[n] / 2.0);
    double total = x * 3 * n;
    cout << setprecision(9) << min(total, w);

    return 0;
}