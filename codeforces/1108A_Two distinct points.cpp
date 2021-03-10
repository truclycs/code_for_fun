#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, l1, r1, l2, r2;
    cin >> n;
    while (n--) {
        cin >> l1 >> r1 >> l2 >> r2;
        int a = l1;
        int b = r2;
        if (a == b) {
            b = l2;
        }
        cout << a << " " << b << "\n";
    }
    return 0;
}