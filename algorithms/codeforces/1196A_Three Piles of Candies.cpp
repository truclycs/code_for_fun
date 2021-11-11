//#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        long long a, b, c;
        cin >> a >> b >> c;
        cout << (a + b + c) / 2 << "\n";
    }
    return 0;
}
