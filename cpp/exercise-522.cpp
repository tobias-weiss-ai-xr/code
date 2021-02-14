#include <iostream>

using namespace std;

int main()
{
    bool bool_value;
    char char_value;
    wchar_t wchar_t_value;
    short short_value;
    int int_value;
    long long_value;
    float float_value;
    double double_value;
    long double long_double_value;

    cout << "Size in bytes:" << endl;
    cout << "bool: " << sizeof(bool_value) << " " <<
            "char: " << sizeof(char_value) << " " <<
            "wchart_t: " << sizeof(wchar_t_value) << " " <<
            "short: " << sizeof(short_value) << " " <<
            "int: " << sizeof(int_value) << " " <<
            "long: " << sizeof(long_value) << " " <<
            "float: " << sizeof(float_value) << " " <<
            "double: " << sizeof(double_value) << " " <<
            "long double: " << sizeof(long_double_value) << endl;

    // Exercise 5.23
    int x[10];
    int *p = x;
    cout << sizeof(x)/sizeof(*x) << endl;
    cout << sizeof(p)/sizeof(*p) << endl;
    return 0;
}

