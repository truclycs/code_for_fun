#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n, x;
    string s;
    cin >> t;
    while (t--) {
        cin >> n >> x >> s; 
        
        int d[n];
        for (int i = 0; i < n; i++) d[i] = 0;
        if (s[0] == '0') d[0] = 1;

        for (int i = 1; i < n; i++) {
            if (s[i] == '0') {
                d[i] = d[i - 1] + 1;
            }
            else {
                d[i] = d[i - 1];
            }
        }

        int val = 2 * d[n - 1] - n;
        int cnt = 0;
        if (x == 0) {
            cnt = 1;
        }
    
        bool flag = false;
        for (int i = 0; i < n; i++) {
            int y = 2 * d[i] - i - 1;
            if (val == 0) {
                if (x - y == 0) {
                    cout << - 1 << "\n";
                    flag = true;
                    break;
                }
                else {
                    continue;
                }
            }
            else {
                int k = (x - y) / val;
                if (k >= 0 && k * val == x - y) {
                    cnt++;
                }
            }
        }
        if (flag) {
            continue;
        }
        cout << cnt << "\n";
    }
    return 0;
}