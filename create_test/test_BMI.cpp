#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        float a, b;
        if (test == 1) {
            a = 1.72;
            b = 55;
        }
        if (test == 2) {
            a = 0.5;
            b = 35;
        }

        if (test == 3) {
            a = 2.5;
            b = 300;
        }
        
        if (test == 4) {
            a = 1.75;
            b = 75;
        }
        
        if (test == 5) {
            a = 1.65;
            b = 95;
        }
        
        if (test == 6) {
            a = 0.9;
            b = 30;
        }
        
        if (test == 7) {
            a = 1.73;
            b = 78;
        }
        
        if (test == 8) {
            a = 1.89;
            b = 100;
        }
        
        if (test == 9) {
            a = 1.25;
            b = 45;
        }
        
        if (test == 10) {
            a = 1.51;
            b = 47;
        }
        
        
        file_in << a << " " << b;
        file_ans << fixed << setprecision(2) << b/ (a *a);
    }
}
