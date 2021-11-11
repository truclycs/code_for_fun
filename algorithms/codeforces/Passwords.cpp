#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<string> pass(n);
    for (int i = 0; i < n; i++) {
        cin >> pass[i];
    }
    string password;
    cin >> password;

    int first_meet = 1;
    int second_meet = 0;
    for (int i = 0; i < n; i++) {
        if (pass[i].size() < password.size()) {
            first_meet++;
        }
        if (pass[i].size() == password.size()) {
            second_meet++;
        }
    }

    second_meet += first_meet - 1;

    int best_case = first_meet + ((first_meet - 1) / k) * 5;
    int worst_case = second_meet + ((second_meet - 1) / k) * 5;

    cout << best_case << " " << worst_case;
    return 0;
}