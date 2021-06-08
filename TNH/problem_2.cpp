#include <bits/stdc++.h>
using namespace std;


string get_numbers(string input_string) {
    string numbers = "";
    for (int i = 0; i < input_string.length(); i++) {
        if (input_string[i] >= '0' && input_string[i] <= '9') {
            numbers += input_string[i];
        } 
    }
    return numbers;
}


string get_result(string numbers) {
    string result, current_string;
    result = numbers[0];
    current_string = "";
    for (int i = 1; i < numbers.length(); i++) {
        if (numbers[i] <= numbers[i - 1]) {
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
    string input_string, numbers;
    cin >> input_string;
    numbers = get_numbers(input_string);
    cout << get_result(numbers);
    return 0;
}