#include <iostream>
#include <vector>

int main(int argc, char const* argv[])
{
	using namespace std;
	vector<int> ivec(7, 42);
	ivec[4] = 7;
	for (vector<int>::iterator i = ivec.begin(); i < ivec.end(); i++) {
		cout << *i << endl;
	}

	// Calculate the middle element
	vector<int>::iterator mid = ivec.begin() - ivec.size() / 2;
	cout << "mid1: " << *mid << endl;

	// This version does not work as there is no arithmetic
	// for an iterator and an int ...
	// mid = ivec.begin() - ivec.end() / 2;

	return 0;
}
