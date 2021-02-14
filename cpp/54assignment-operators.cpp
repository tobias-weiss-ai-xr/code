#include <iostream>

using namespace std;

int get_value(){
    int i;
    while (!is_integral(i)) {
        cout << "Bitte geben Sie eine Zahl ein: " << endl;
        cin >> i;
    }
    
}

int main (){
    int val = get_value();
}
