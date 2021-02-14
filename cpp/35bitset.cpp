#include <bitset>
#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
	bitset<32> bitvec; // 32 bits, all zero
	bool is_set = bitvec.any(); // false, all bits are zero
	bool is_not_set = bitvec.none(); // true
	// how many bits are set?
	size_t bits_set = bitvec.count(); // returns number of bis that are on
	// get the size_t
	size_t sz = bitvec.size();

	// assign 1 ot even numbered bits
	for (int i = 0; i != bitvec.size(); i+=2) {
		bitvec[i] = 1;
		// bitvec.set(index); // does the same
	}

	// test if bit is on
	if (bitvec[1]) {
		// bitvec 1 is on
	}
	if (bitvec.test(1)){
		// also tests if 1 is set
	}
	
	// set the entire bitset
	bitvec.reset(); // sets all bits to 0
	bitvec.set(); // sets all bits to 1

	// flip some bits
	bitvec.flip(0); // reverse value of first bit
	bitvec[0].flip(); // also reverse first bit
	bitvec.flip(); // reverse all bits

	// retrieve the value of a bitset
	unsigned long ulong = bitvec.to_ulong();
	cout << "ulong = " << ulong << endl;

	// print the bits 
	bitset<32> bitvec2(0xffff); // bit 0 ... 15 are set to 1; 16 ... 31 are 0
	cout << "bitvec2: " << bitvec2 << endl;

	//exercises
	bitset<64> bitvec3(32);
	bitset<32> bv(1010101);
	string btstr; cin >> btstr; bitset<8> bv2(btstr);

	cout << "bitvec3: " << bitvec3 << endl;
	cout << "bv: " << bv << endl;
	cout << "bv2: " << bv2 << endl;

	return 0;
}
