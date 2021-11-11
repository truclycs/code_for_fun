#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n);
    for (int i = 0; i < n; i++) {
        cin >> t[i];
    }

    int Alice = 0;
    int Bob = 0;
    int l = 0;
    int r = n - 1;
    while (l <= r) {
        if (Alice <= Bob) {
            Alice += t[l];
            l++;
        }
        else {
            Bob += t[r];
            r--;
        }
    }    

    cout << l << " " << n - l;

    return 0;
}