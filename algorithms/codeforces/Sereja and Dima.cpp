#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int Sereja = 0;
    int Dima = 0;
    int l = 0, r = n - 1;
    while (l <= r) {
        if (a[l] > a[r]) {
            Sereja += a[l];
            l++;
        }
        else {
            Sereja += a[r];
            r--;
        }

        if (l > r) {
            break;
        }

        if (a[l] > a[r]) {
            Dima += a[l];
            l++;
        }
        else {
            Dima += a[r];
            r--;
        }
    }

    cout << Sereja << " " << Dima;

    return 0;
}