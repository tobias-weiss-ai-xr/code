#include <iostream>
#include <string>

std::string s1 = "hello"; // s1 has global scope
int main(){
    std::string s2 = "world"; // s2 has local scope
    std::cout << s1 << " " << s2 << std::endl; // uses global s1
    int s1 = 42;
    std::cout << s1 << " " << s2 << std::endl; // uses local s1, hides global s1
    return 0;
}