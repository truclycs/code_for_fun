#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str()); 
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 1001;
        int b = rand() % 2;
        if (b) {
            a*=-1;
        }
        if (test == 1) a = 45;
        if (test == 2) a = 1000;
        if (test == 3) a = -1000;
        if (test == 4) a = 0;
        float pi = 3.14;
        float d = (float)(pi * a) / 180.0;
        file_ans << fixed << setprecision(4) << cos(d);
        file_in << a;
    }
}