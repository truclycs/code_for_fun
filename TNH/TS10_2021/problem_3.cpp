#include <iostream>
using namespace std;


bool is_palin(string s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }
    return true;
}


int main() {
    string s, sub_s;
    cin >> s;

    string result = "";
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            sub_s = s.substr(j, i + 1);
            if (is_palin(sub_s)) {
                result = sub_s;
            }
        }
    }

    cout << result;
    return 0;
}