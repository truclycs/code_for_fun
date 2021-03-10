#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int m = 100000;
        int n = rand() % m + 1;;
        if (test == 1) {
            n = 5;
            m = 10;
        }
        if (test == 6) n = 100000;
        file_in << n << endl;
        int a[n];
        for (int i = 0; i < n - 1; i++) {
            a[i]= rand() % m + 1;
            file_in << a[i] << " ";
        }

        a[n - 1] = rand()%m + 1;
        file_in << a[n - 1];
            for (int i = n - 1; i > 0; i--) {
        file_ans<< a[i] << " ";
    }
    file_ans << a[0];
    }
}

