#include<bits/stdc++.h>
using namespace std;

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    string s;
    cin >> s;

    int res = 0;
    int pre = 'a';
    for (int i = 0; i < s.size(); i++) {
        int dist = abs(s[i] - pre);
        if (dist < 13) {
            res += dist;
        }
        else {
            res += (26 - dist);
        }
        pre = s[i];
    }

    cout << res;
    return 0;
}