#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    string s;
    cin >> n >> k >> s;
    if (n == 1) {
        (k > 0) ? cout << 0 : cout << s;
    }
    else {
        if (k) {
            if (s[0] != '1') {
                s[0] = '1';
                k--;
            }
        }
        int i = 1;
        for (int j = 0; j < k; j++) {
            while (s[i] == '0' && i < s.size()) {
                i++;
            }
            s[i] = '0';
            if (i >= s.size()) {
                break;
            }
        }
        cout << s;
    }
    return 0;
}