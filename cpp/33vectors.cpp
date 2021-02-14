#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
	vector<int> ivec;
	vector<string> svec;

	vector<int> ivec2(ivec); // Copy of ivec
	vector<int> ivec3(2,3); // Holds 2 int values (3,3)
	// vector<string> svec2(ivec); // Error: A string from an int oO
	vector<string> svec3(10, "Hi!"); // Holds 10x hi...

	vector< vector<int> > ivec4; // nested vector
	
	string text;
	while (cin >> text) {
		if (text == "EOF") {
			break;
		}
		svec.push_back(text);
	}

	for (vector<string>::size_type index = 0; index != text.size(); index++) {
		cout << svec[index] << endl;;
	}

	vector<int> ivec5;
	// CAVEAT: elements can not be added via a new index!
	// for (vector<int>::size_type ix = 0; ix != 10; ix++) {
	// 		ivec5[ix] = ix;
	//}
	
	// one has to use the push_back function
	for (vector<int>::size_type ix = 0; ix < 10; ix++) {
		ivec5.push_back(ix);
	}		
	return 0;
}
