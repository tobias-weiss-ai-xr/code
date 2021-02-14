#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const* argv[])
{
	const size_t arr_size = 5;
	int int_arr[arr_size] = {0, 1, 2, 3, 4};

	// pbegin points to the first element and pend to the off-by-one element of the array

	//set all values to zero
	for(int *pbegin = int_arr, *pend = int_arr + arr_size; pbegin != pend; ++pbegin)
		*pbegin=0;

	//print all values
	for (int *pbegin = int_arr, *pend = int_arr + arr_size; pbegin != pend; ++pbegin) {
		std::cout << *pbegin << ' '; // print the current element
	}
	std::cout << std::endl;

	// const pointer
	int errNumb = 0;
	int *const curErr = &errNumb; // curerr is a constant pointer (can't point to anything else)
	*curErr = 1; // The value of the element pointed to still can be altered
	
	// pointers and typedefs	
	typedef string 	*pstring; // *pstring is a string
	string test = "test";
	const pstring cstr = &test;//What is the type of cstr?
	// Wrong interpretation:
	// const string cstr;
    // Right interpretation:
	// string *const cstr;
	

	string const s1; // s1 and s2
	const string s2; // both are strings that are const...


	return 0;
}
