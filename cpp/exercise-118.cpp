#include <iostream>

int main(int argc, char const *argv[])
{
    int min, max, counter=0;
    std::cout << "Please enter min. Number: " << std::endl;
    std::cin >> min;
    std::cout << "Please enter max. Number: " << std::endl;
    std::cin >> max;
    for (int i = min; i <= max; i++)
    {
        if (counter>9)
            break;
        std::cout << i << " ";
        counter++;
    }
    std::cout << std::endl;
    return 0;
}