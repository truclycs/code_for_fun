#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("alchemy_input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, n;
    string s;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> n >> s;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'A') {
                cnt++;
            }
        }
        if (abs(cnt - (n - cnt)) == 1) {
            cout << "Case #" << t <<": "<< "Y\n";
        }
        else {
            cout << "Case #" << t <<": "<< "N\n";        
        }
    }
    return 0;
}
