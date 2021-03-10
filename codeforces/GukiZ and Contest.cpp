#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a.begin(), a.end(), greater<pair<int, int>>());

    vector<int> rank(n);
    rank[a[0].second] = 1;
    for (int i = 1; i < n; i++) {
        if (a[i].first < a[i - 1].first) {
            rank[a[i].second] = i + 1;
        }
        else {
            rank[a[i].second] = rank[a[i - 1].second];
        }
    }

    for (int i = 0; i < n; i++) {
        cout << rank[i] << " ";
    }

    return 0;
}