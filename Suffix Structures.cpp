#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;

    vector<int> cnt_s(26, 0), cnt_t(26, 0);
    for (int i = 0; i < s.size(); i++) {
        cnt_s[s[i] - 'a']++;
    }

    for (int i = 0; i < t.size(); i++) {
        cnt_t[t[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (cnt_s[i] < cnt_t[i]) {
            cout << "need tree";
            return 0;
        } 
    }

    bool automaton = true;
    int j = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == t[j]) {
            j++;
        }
    }

    if (j < t.size()) {
        automaton = false;
    }

    if (s.size() == t.size()) {
        cout << "array";
    }
    else if (automaton) {
        cout << "automaton";
    }
    else {
        cout << "both";
    }

    return 0;
}