#include <iostream>

int main(int argc, char const* argv[])
{
	const short size = 3; // array size must be constant!
	int ia[size] = {1, 2, 3}; // values in curly brackes
	int ib[] = {1, 2}; // size infered from number of elements given

	// char arrays are special
	char cha1[] = {'C', '+', '+'}; // no null
	char cha2[] = {'C', '+', '+', '\0'}; // explicit null
	char cha3[] = "C++"; // null automatically added

	const size_t array_size = 10;
	int ia1[array_size]; // 10 ints, elements are uninitialized
	
	// loop through the array and assign the index as values
	// of the elements
	for (size_t i = 0; i < array_size; i++) {
		ia1[i] = i;
	}

	// Copy the array
	int ia2[array_size];
	for (size_t i = 0; i < array_size; i++) {
		ia2[i] = ia1[i];	
	}

	return 0;
}
