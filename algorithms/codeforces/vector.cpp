#include <iostream>
#include <vector>  
using namespace std;

int main() {
    vector<int> v;  //vector<data_type> name;
    
    v.push_back(10); //push_back(value): Them phan tu 
    
    cout << v.front() << " " << v[0] << "\n"; //Lay phan tu dau tien

    cout << v.size() << "\n"; //Lay kich thuoc
    
    v.resize(2); //Thay doi kich thuoc, cac phan tu them mac dinh = 0

    //Kiem tra vector co rong hay khong?

    if (v.empty() == true) {
        cout << "empty\n";
    }
    else {
        cout << "not empty\n";
    }

    //Chen 1 gia tri vao vector: insert(iterayor, value)
    vector<int>::iterator it;
    it = v.begin() + 1;
    v.insert(it, 5);

    //Chen hang loat gia tri: insert(iterator, size_type, value)
    it = v.begin() + 2;
    v.insert(it, 3, 4);

    v.pop_back(); // Xoa phan tu cuoi

    // Xoa phan tu bat ki
    it = v.begin() + 1;
    v.erase(it);

    // Xoa hang loat phan tu
    vector<int>::iterator it1;
    vector<int>::iterator it2;
    it1 = v.begin() + 1;
    it2 = v.begin() + 3;
    v.erase(it1, it2);

    v.clear(); // Xoa toan bo vector

    //Duyet qua cac phan tu trong vector
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }

    //Vector nhu mang 2 chieu

    vector<vector<int>> a; //vector<vector<data_type>> name;
    int n = 3;
    int m = 3;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        a[i].resize(m);
        for (int j = 0; j < m; j++) {
            a[i][j] = 1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] << " ";
        }
        cout << "\n";
    }

    vector<int> arr(5);
    for (int i = 0; i < 5; i++) {
        arr[i] = i;
    }

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    cout << "\n";

    vector<int> vec(5, 1);

    for (int i = 0; i < 5; i++) {
        cout << vec[i] << " ";
    }

    return 0;
}