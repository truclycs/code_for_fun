#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int n = rand() % 100 + 1;
        if (test == 1) {
            n = 4;
        }
        if(test == 2) n = 100;
        file_in << n;
        for (int i = n; i >= 1; i--) {
        for (int j = 0; j < i; j++) {
            file_ans << "#";
        }
        file_ans
         << "\n";
    }
    }
}
