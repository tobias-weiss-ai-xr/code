#include <iostream>

using namespace std;

int main()
{
    int i;
    double d;
    int *p = &i;

    d = i = 3.5;
    cout << "d: " << d << " i: " << i << endl;

    i = d = 3.5;
    cout << "d: " << d << " i: " << i << endl;

    // ex 514
    // d = i = p = 0; // Illegal as the pointer must be dereferenced
    d = *p = i = 0;
    cout << "d: " << d << " i: " << i << "p: " << *p << endl;

    return 0;
}

