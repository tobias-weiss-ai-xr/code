#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> ivec;
    int cnt = 10;
    // add elements 10..1
    while (cnt > 0) {
        ivec.push_back(cnt--); // post fix notation. returned value is still the old.
    }

    vector<int>::iterator iter = ivec.begin();
    // print all elements
    while (iter != ivec.end()) {
        cout << *iter++ << endl; // is interpreted as *(iter++) as ++ has higher precedence
    }

    return 0;
}

