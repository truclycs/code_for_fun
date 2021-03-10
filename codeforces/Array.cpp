#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    vector<int> d(100001, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int cnt = 0;
    int l = 0;
    int left = -1, right = -1;
    for (int r = 0; r < n; r++) {
        d[a[r]]++;
        if (d[a[r]] == 1) {
            cnt++;
            if (cnt == k) {
                while (d[a[l]] != 1) {
                    d[a[l]]--;
                    l++;
                }
                left = l + 1;
                right = r + 1;
                break;
            }
        }
    }

    cout << left << " " << right; 
    return 0;
}