#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int s = rand() % 100000 + 1;
        int a = rand() % 100000 + 1;
        int b = rand() % 100000 + 1;
        if (test == 1) {
            s = 15;
            a = 2;
            b = 6;

        }
        if (test == 2) {
            s = 6;
            a = 4;
            b = 2;
        }
        if (test == 3) {
            s = 100000;
            a = 100000;
            b = 100000;
        }
                if (test ==4) {
            s = 100000;
            a = 1;
            b = 2;
        }
        file_in << s << " " << a <<" " << b;
        	float t = (float)s / (b + a);
	file_ans << fixed << setprecision(2) << t;
    }
}
