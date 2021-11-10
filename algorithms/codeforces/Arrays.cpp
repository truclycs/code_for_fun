#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int na, nb, k, m, x;
    vector<int> a, b;
    
    cin >> na >> nb >> k >> m;

    for (int i = 0; i < na; i++) {
        cin >> x;
        a.push_back(x);
    }
    
    for (int i = 0; i < nb; i++) {
        cin >> x;
        b.push_back(x);
    }

    if (a[k - 1] < b[nb - m]) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    
    return 0;
}