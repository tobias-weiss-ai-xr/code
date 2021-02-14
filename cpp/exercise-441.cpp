#include <iostream>

int main(int argc, char const* argv[])
{
	const size_t rowSize = 3;
	const size_t colSize = 4;
	int ia [rowSize][colSize]; // 12 uninitialized elements
	// for each row
	for (size_t i = 0; i != rowSize; ++i) {
		// for each column within the rowSize
		for (size_t j = 0; j != colSize; ++j) {
			// initialize to its positional index
			ia[i][j] = i * colSize + j;
			std::cout << ia [i][j] << std::endl;
		}
	}
	return 0;
}
