#include <bits/stdc++.h>
using namespace std;
bool d[1000000];
int dis[100005];

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % 2 == 0) {
            return false;
        }
    }
    return true;
}

int stepsToPrime(int n) {
    if (n == 0) {
        return 0;
    }
    for (int i = 0; i < 1000000; i++) {
        d[i] = true;
    }
    queue<int> q;
    q.push(n);
    dis[n] = 0;
    d[n] = false;
    while (!q.empty()) {
        int p = q.front();
        if (isPrime(p)) {
            return dis[p];
        }
        q.pop();
        int x = p;
        while (x != 0) {
            int tmp = x % 10;
            if (d[tmp + p]) {
                d[tmp + p] = false;
                q.push(tmp + p);
                dis[tmp + p] = dis[p] + 1;
            }
            if (p - tmp > 0 && d[p - tmp]) {
                d[p - tmp] = false;
                q.push(p - tmp);
                dis[p - tmp] = dis[p] + 1;
            }
            x /= 10;
        }
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < 1000000; i++) {
        d[i] = true;
    }
    cout << solve(n);
    return 0;
}
