#include<bits/stdc++.h>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;

    int n = s.size() - 1;
    while (s[n] == 'z') {
        s[n] = 'a';
        n--;
    }

    s[n] += 1;

    if (s < t) {
        cout << s;
    }
    else {
        cout << "No such string";
    }

    return 0;
}