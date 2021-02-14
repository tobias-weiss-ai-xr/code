#include <iostream>
#include <bitset>

using namespace std;

int main()
{
    bitset<30> bitset_quiz1; // bitset solution
    unsigned long int_quiz1 = 0; // simulated collection of bitset

    bitset_quiz1.set(27); // indicate student 27 passed - zero based, I think the textbook messes with the index!
    cout << bitset_quiz1 << endl;
    int_quiz1 |= 1UL<<27; // inidcate student 27 passed (shift 1 to position 27)
    int_quiz1 = int_quiz1 | 1UL<<27; // equivalent to statement above

    bitset_quiz1.reset(27); // indicate student 27 failed
    int_quiz1 &= ~(1UL<<27); // inidcate student 27 passed (shift 1 to position 27). A bitwise and leaves all other bits unchanged

    bool status;
    status = bitset_quiz1[27];
    status = int_quiz1 & (1UL<<27); // equivalent to statement above

    unsigned long ul1 = 3, ul2 = 7; // Exercise 5.9
    cout << bitset<16>(ul1) << endl;
    cout << bitset<16>(ul1 & ul2) << endl; // bitwise and
    cout << (ul1 && ul2) << endl; // logical and
    cout << bitset<16>(ul1 | ul2) << endl; // bitwise or
    cout << (ul1 || ul2) << endl; // logical or

    cout << bitset_quiz1 << endl; // Exercise 5.10
    bitset_quiz1[0] = 1; // inidcate student 27 passed - zero based!
    bitset_quiz1[27] = 1; // inidcate student 27 passed
    cout << bitset_quiz1 << endl;

    return 0;
}
