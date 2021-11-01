#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int n = rand() % 1000000 + 1;

        if (test == 1) {
            n = 5;
        }

        if (test == 2) {
            n = 1000000;
        }

        file_in << n;
        for (int i = 1; i <= n; i++) {
            file_ans << i << " ";
        }
    }
}
