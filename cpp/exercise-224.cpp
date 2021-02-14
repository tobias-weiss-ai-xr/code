#include <iostream>

int main(int argc, char const *argv[])
{
    int ival = 1.01;
    // not working as it is pointing nowhere 
    // int &rval1 = 1.01;
    int &rval2 = ival;
    const int &rval3 = 1.01;

    int i, &ri = i;
    i = 5; ri = 10; // the assignment of the pointer is stored in the variable memory location (it is "overwritten")
    std::cout << i << " " << ri << std::endl;

    return 0;
}