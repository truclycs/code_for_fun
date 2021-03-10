#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        int N = rand() % 100000000 + 1;
        N *= 10;
        if (test == 1) N = 12340;
        if (test == 2) N = 1000000000;
        file_in << N;
        	file_ans << N / 500 << " ";
	N = N % 500;
	file_ans << N / 200 << " ";
	N = N % 200;
	file_ans << N / 100 << " ";
	N = N % 100;
	file_ans << N / 50 << " ";
	N = N % 50;
	file_ans << N / 20 << " ";
	N = N % 20;
	file_ans << N / 10;

}

}