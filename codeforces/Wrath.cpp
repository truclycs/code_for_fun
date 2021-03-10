#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << 1;
        return 0;
    }

    int alive_people = 1;
    int people = a[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        if (people == 0) {
            alive_people++;
        }
        else {
            people--;
        }
        people = max(people, a[i]);
    }

    cout << alive_people;
    return 0;
}