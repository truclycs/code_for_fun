#include<iostream>
using namespace std;


int main() {
    int n;
    int a[1000000];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0 && a[i] % 5 == 0 && a[i] > result) {
            result = a[i];
        }
    }

    cout << result;
    return 0;
}