#include <iostream>
#include <vector>

using namespace std;

int main()
{
    string s1 = "s", s2 = "s2", s3 = "s33";
    vector<string> spvec; // vector of pointers

    spvec.push_back(s1);
    spvec.push_back(s2);
    spvec.push_back(s3);

    for (vector<string>::iterator iter = spvec.begin(); iter != spvec.end(); ++iter) {
        cout << *iter << " length: " << iter->size() << endl;
    }

    return 0;
}

