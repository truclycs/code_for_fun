#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    int n = x % 4;
    if (n == 1) {
        cout << "0 A";
    }
    else if (n == 2) {
        cout << "1 B";
    }
    else if (n == 3) {
        cout << "2 A";
    }
    else {
        cout << "1 A";
    }
    return 0;
}