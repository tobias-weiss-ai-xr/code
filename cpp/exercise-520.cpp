#include <iostream>

using namespace std;

int main()
{
    int i1, i2;
    cout << "Please enter two numbers: ";
    cin >> i1 >> i2;
    cout << ( i1 < i2 ? i1 : i2) << " is smaller than " << ( i1 < i2 ? i2: i1 ) << "." << endl; //The paranthesis are mandatory!
    return 0;
}

