#include <iostream>

int main(int argc, char const *argv[])
{
    int value = 0;
    int count = 0;
    // loop until no more input is given
    while (std::cin >> value)
    {
        // count negative values
        if (value < 0)
        {
            count++;
        }
    }
    std::cout << "The amount of negative numbers is "
              << count
              << std::endl;
    return 0;
}