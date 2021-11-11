#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n], d[n] = {false};
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a, a + n);
    int res = 0;

    for (int i = 0; i < n; i++) {
        if (!d[i]) {
            res++;
            for (int j = i + 1; j < n; j++) {
                if (a[j] % a[i] == 0) {
                    d[j] = true;
                }
            }
        }
    }

    cout << res;
    return 0;
}
