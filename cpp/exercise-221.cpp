#include <iostream>

int sum = 0;
int main(int argc, char const *argv[])
{
    for (int i = 0; i != 10; ++i)
        sum += i;
    // Errorous as i is tried to be printed
    // outside of its scope.
    std::cout << "Sum from 0 to " << i 
            << " is " << sum << std::endl;
    return 0;
}
