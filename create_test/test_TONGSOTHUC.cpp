#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int n = rand() % 10000000 + 1;

        float a, b;
        a = (float)(n) / 31;
        b = (float)(n) / 17;
        if (test == 1) {
            a = 2.2525;
            b = 4.275;
        }
        if (test == 2) {
            a = 1000000;
            b = 1000000;
        }
        file_in << a << " " << b;
        file_ans << fixed << setprecision(4) << a + b;
    }
}
