#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 1000 + 1;
        int b = rand() % 1000 + 1;

        if (test == 1) {
            a = 5;
            b = 4;
        }
        if (test == 2) {
            a = 1000;
            b = 1000;
        }
                if (test == 3) {
            a = 1000;
            b = 1;
        }
                if (test == 4) {
            a = 1;
            b = 1000;
        }
        file_in << a << " " << b;
        file_ans<< fixed << setprecision(2) << a << " / " << b << " = " << (float)a / (float)b;
    }
}
