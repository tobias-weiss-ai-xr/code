#include <iostream>
#include <bitset>
#include <vector>

using namespace std;

int main(int argc, char const* argv[])
{
	vector<int> fib;
	fib.push_back(1);
	fib.push_back(2);
	fib.push_back(3);
	fib.push_back(5);
	fib.push_back(8);
	fib.push_back(13);
	fib.push_back(21);
	bitset<32> bs;
	for (vector<int>::iterator ix = fib.begin(); ix != fib.end() ; ix++) {
		bitset<32> tmp(*ix);
		for (int jx = 0; jx != 32; jx++) {
			if (tmp.test(jx)) {
				bs.set(jx);
			}
		}
	}
	cout << "bs: " << bs << " and in ulong: " << bs.to_ulong() << endl;

	return 0;
}
