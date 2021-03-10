#include <bits/stdc++.h>
using namespace std;
 
int main() {
    // freopen("inp.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    for (int i = 0; i < n; i++) {
        cout << n - a[i] + 1 << " ";
    }
    return 0;
}