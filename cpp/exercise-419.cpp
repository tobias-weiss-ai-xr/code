#include <iostream>

using namespace std;

int main(int argc, char const* argv[])
{
	int i = 42;
	const int ic = 42;
	const int *pic = &ic; // can point to an int that is const
	cout << "pic: " << *pic << endl; // Leading to seg fault...
	int *const cpi = &i; // constant pointer (own value may not be changed)
	i = 43; // The variable to which it points still can be altered
	const int *const cpic = &ic; // constant pointer to a const
	return 0;
}
