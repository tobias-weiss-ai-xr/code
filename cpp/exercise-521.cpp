#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v1;
    for (int i = 0; i != 10; ++i) {
        v1.push_back(i);
    }
    for (vector<int>::iterator iter = v1.begin(); iter != v1.end(); ++iter) {
        *iter = (*iter % 2 == 0 ? *iter : *iter * 2); // Check if value is odd and multiply if true with two in order to make it even
        cout << *iter << endl; // Output the even values. Snygg!!
    }
    
    return 0;
}

