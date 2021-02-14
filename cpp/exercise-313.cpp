#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const* argv[])
{
	vector<int> ivec;
	cout << "Enter some integers (escape by -1): " << endl;
	int input;
	while (cin >> input) {
		if (input == -1) {
			break;
		}	
		ivec.push_back(input);
	}
	for (vector<int>::size_type ix = 0; ix != ivec.size(); ix=ix+2) {
		if (ix == ivec.size()-1) {
			cout << "The amount of values is odd." << endl;
			cout << ivec[ix] << endl;
			break;
		}
		cout << ivec[ix] + ivec[ix+1] << endl;
	}
	return 0;
}
