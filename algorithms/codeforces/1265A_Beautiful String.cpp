#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;

        bool flag = false;
        char res[s.size()];
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1] && s[i] != '?') {
                cout << - 1 << "\n";
                flag = true;
                break;
            }
        }
        
        if (s.size() == 1 && s[0] == '?') {
            cout << 'a' << "\n";
            flag = true;
        } 

        if (flag) {
            continue;
        }


        if (s[0] == '?') {
            if (s[1] != 'a') {
                res[0] = 'a';
            }
            else if (s[1] != 'b') {
                res[0] = 'b';
            }
            else {
                res[0] = 'c';
            }
            s[0] = res[0];
        }  
        else {
            res[0] = s[0];
        }

        int n = s.size();
        if (s[n - 1] == '?') {
            if (s[n - 2] != 'a') {
                res[n - 1] = 'a';
            }
            else if (s[n - 2] != 'b') {
                res[n - 1] = 'b';
            }
            else {
                res[n - 1] = 'c';
            }
            s[n - 1] = res[n - 1];
        }  
        else {
            res[n - 1] = s[n - 1];
        }

        for (int i = 1; i < n - 1; i++) {
            if (s[i] == '?') {
                if (s[i - 1] != 'a' && s[i + 1] != 'a') {
                    res[i] = 'a';
                    s[i] = res[i];
                }
                else if (s[i - 1] != 'b' && s[i + 1] != 'b') {
                    res[i] = 'b';
                    s[i] = res[i];
                }
                else if (s[i - 1] != 'c' && s[i + 1] != 'c') {
                    res[i] = 'c';
                    s[i] = res[i];
                }
                else {
                    flag = true;
                    break;
                }
            }
            else {
                res[i] = s[i];
            }
        }

        if (flag) {
            cout << "-1\n";
        }
        else {
            for (int i = 0; i < n; i++) {
                cout << res[i]; 
            }
            cout << endl;
        }
    }
    return 0;
}