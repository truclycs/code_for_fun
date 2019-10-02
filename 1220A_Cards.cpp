#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string s;
    cin >> N >> s;
    int z = 0, e = 0, r = 0, o = 0, n = 0;
    for (int i = 0; i < N; i++) {
        if (s[i] == 'z') z++;
        if (s[i] == 'e') e++;
        if (s[i] == 'r') r++;
        if (s[i] == 'o') o++;
        if (s[i] == 'n') n++;
    }
    int one = min(min(o, n), e);
    o -= one;
    n -= one;
    for (int i = 0; i < one; i++) {
        cout << 1 << " ";
    }
    for (int i = 0; i < min(min(min(z, e), r), o); i++)  {
        cout << "0 ";
    }
    return 0;
}