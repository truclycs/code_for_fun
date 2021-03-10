#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 100;
        int b = rand() % 100;
        if (test == 1) {
            a = 90;
            b = 19;
        }
        file_in << a << " " << b;
        file_ans << (b + 2000) - (a + 1900);
    }
}
