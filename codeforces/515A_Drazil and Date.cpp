#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, s;
    cin >> a >> b >> s;
    int t = s - (abs(a) + abs(b));
    if (t >= 0 && t % 2 == 0) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}