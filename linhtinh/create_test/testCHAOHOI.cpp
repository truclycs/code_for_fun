	#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int test = 1; test <= 10; ++test) {
        ofstream file_in((std::to_string(test) + ".in").c_str());
        ofstream file_ans((std::to_string(test) + ".ans").c_str());
        string s;
        int a, b;
        if (test == 1) {
            s = "Tom" ;
        }
        if (test == 2) {
            s = "klsjfoizsndfnioawefjknsdkjfkjsbfksbduidx";
            a = 0;
            b = 1000;
        }
        if (test == 3) {
            s = "knfKJLKNnmnsgkng";
            a = -100;
            b = 1;
        }
                if (test ==4) {
            s = "kjshfJBJF";
            a = 100;
            b = 1;
        }
        if (test == 5) s = "LYLYLYLYLYLY";
        if (test == 6) s =  "abcabcdegh";
        if (test == 7) s =  "abcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdeghabcabcdegh";
        if (test == 8) s =  "nhcngttnhuot";
        if (test == 9) s =  "lkfjsdfsdfKJGSHJKSNGklsngjkadrg";
        if (test == 10) s =  "QUJhdnsflsdfhalkdjsfslnelsvrdtvosieruhfjksdfnb";
        file_in << s;
		file_ans << "Hello, " << s << ". How are you today?";
    }
}



