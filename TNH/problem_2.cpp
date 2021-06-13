#include <iostream>
using namespace std;


string get_numbers(string s) {
    string numbers = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            numbers += s[i];
        } 
    }
    return numbers;
}


string get_result(string numbers) {
    string result, current_string;
    result = numbers[0];
    current_string = "";
    for (int i = 1; i < numbers.length(); i++) {
        if (numbers[i - 1] >= numbers[i]) {
            current_string += numbers[i];
            if (result.length() < current_string.length()) {
                result = current_string;
            }
        }
        else {
            current_string = numbers[i];
        }        
    }
    return result;
}


int main() {
    string s, numbers;
    cin >> s;
    numbers = get_numbers(s);
    cout << get_result(numbers);
    return 0;
}