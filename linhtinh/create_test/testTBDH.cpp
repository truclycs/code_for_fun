	#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int a = rand() % 1000 + 1;
        int b = rand() % 1000 + 1;
        int s;
        if (test == 1) {
            s = 2 ;
            a = 6;
            b = 3;

        }
        if (test == 2) {
            s = 6;
            a = 1000;
            b = 1000;
        }
        if (test == 3) {
            s = 100000;
            a = 1;
            b = 1;
        }
                if (test ==4) {
            s = 100000;
            a = 1000;
            b = 1;
        }
        file_in << a <<" " << b;
	file_ans << fixed << setprecision(4) << sin(a);
    }
}



