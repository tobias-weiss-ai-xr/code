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
	for (vector<int>::size_type ix = 0; ix <= ivec.size()/2; ix++) {
		if (ix == (ivec.size()/2) && ivec.size() % 2 != 0) {
			cout << "The amount of values is odd." << endl;
			cout << ivec[ix] << endl;
			break;
		}
		cout << ivec[ix] + ivec[(ivec.size()-1-ix)] << endl;
	}
	return 0;
}
