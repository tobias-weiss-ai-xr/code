#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
	int i = -1; // simple int
	const int ic = i; // a constant
	const int *pic = &ic; // pointer to a const
	// int *const cpi = &ic; // wrong const pointers value might be changed
	const int *const cpic = &ic; // const pointer to const 

	// 4.21
	i = ic; // legal
	pic = &ic; // legal - variable gets address of ic
	pic = cpic; // legal
	// ic = *cpic; // illegal - const can't be reassigned...

	cout << *pic << endl;

	return 0;
}
