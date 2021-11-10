#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    string s;
    cin >> t;
    while (t--) {
        cin >> s;
        char c = s[s.size() - 1];
        if (c == 'o') {
            cout << "FILIPINO\n"; 
        }
        else if (c == 'u') {
            cout << "JAPANESE\n";
        }
        else {
            cout << "KOREAN\n";
        }
    }
    return 0;
}