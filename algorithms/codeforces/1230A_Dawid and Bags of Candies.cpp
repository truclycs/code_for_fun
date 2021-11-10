#include <bits/stdc++.h>
using namespace std;
int b[4], a[4];
bool flag = false;

void back(int i) {
    for (int j = 0; j <= 1; j++) {
        b[i] = j;
        if (i == 3) {
            int x = 0;
            int y = 0;
            for (int k = 0; k < 4; k++) {
                if (b[k]) {
                    x += a[k];
                }
                else {
                    y += a[k];
                }
            }
            if (x == y) {
                flag = true;
            }
        }
        else {
            back(i + 1);
        }
    }
}

int main() {
    cin >> a[0] >> a[1] >> a[2] >> a[3];
    back(0);
    if (flag) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}