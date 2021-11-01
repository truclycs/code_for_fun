#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 100 + 1;
        int b = rand() % 100 + 1;

        if (test == 1) {
            a = 4;
            b = 5;
        }
        if (test == 2) {
            a = 100;
            b = 100;
        }
        if (test == 3) {
            a = 1;
            b = 1;
        }
    
        file_in << a << " " << b;
        file_ans << fixed << setprecision(2) << sqrt(a * a + b * b + 2 * sqrt(a * b));
    }
}
