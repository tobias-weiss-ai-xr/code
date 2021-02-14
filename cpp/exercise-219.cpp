#include <iostream>

int main(int argc, char const *argv[])
{
    int i = 100, sum = 0;
    for (int i = 0; i <=10 ; ++i)
    {
        // i is shadowed by local i
        sum += 1;
    }
    // prints the global i and the calculated sum
    std::cout << i << " " << sum << std::endl; 
    return 0;
}