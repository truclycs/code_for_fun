#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str()); 
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int D = rand() % 51;
        int W = rand() % 51;
        int L = rand() % 31;
        if (test == 1) {
            D = 10;
            W = 15;
            L = 13;
        }

                if (test == 2) {
            D = 0;
            W = 0;
            L = 0;
        }

                if (test == 3) {
            D = 50;
            W = 50;
            L = 50;
        }
        file_in << W << " " << D << " " << L;
        file_ans << W * 3 + 1 * D + 0 * L;
    }
}