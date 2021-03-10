#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 100 + 1;
        int b = rand() % 100 + 1;
        int c = rand() % 100 + 1;

        if (test == 1) {
            a = 3;
            b = 4;
            c = 5;
        }
        if (test == 2) {
            a = 100;
            b = 100;
            c = 100;
        }
               if (test == 3) {
            a = 1;
            b = 1;
            c = 1;
        }

        file_in << a << " " << b << " " << c;
        file_ans<< a*b*c;
    }
}
