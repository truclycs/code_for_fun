#include <iostream>
using namespace std;


int main() {
    int x, result;
    cin >> x;
    
    if (x <= 50) {
        result = x * 1678;
    } else if (x <= 100) {
        result =  (50 * 1678 + (x - 50) * 1734);
    } else if (x <= 200) {
        result = (50 * 1678 + 50 * 1734 + (x - 100) * 2014);
    } else if (x <= 300) {
        result = (50 * 1678 + 50 * 1734 + 100 * 2014 + (x - 200) * 2536);
    } else if (x <= 400) {
        result = (50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (x - 300) * 2834);
    } else {
        result = (50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (x - 400) * 2927);
    }

    result = int(result * 1.1);

    cout << result;

    return 0;
}