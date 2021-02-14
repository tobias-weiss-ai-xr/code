#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const* argv[])
{
	const size_t arr_size = 10;
	int ia[arr_size];

	// initialize the array with index values
	vector<int> ivec;
	for (size_t index = 0; index != arr_size; index++) {
		ia[index] = index;
		ivec.push_back(index);
	}

	// make a copy of the array
	int ia2[arr_size];
	for (size_t index = 0; index != arr_size; index++) {
		ia2[index] = ia[index];
	}
	// a vector is much easier to copy...
	vector<int> ivec2 = ivec;

	// check if two arrays are equal
	bool arr_equal = true;
	for (size_t index = 0; index != arr_size; index++) {
		if (ia[index] != ia2[index]) {
			arr_equal = false;
			break;
		}
	}
	if (arr_equal) {
		cout << "the arrays are equal" << endl;
	}

	if (ivec == ivec2) {
		cout << "the vectors are equal" << endl;
	}

	string s = "hello world!";
	string *sp = &s; // sp holds the address of s

	// declaration of different pointer types
	vector<int> *pvec = 0;
	int *ip, ip2;
	string *pstring;
	double *dp;

	int iv, *ip3; // object and pointer declarations can be mixed

	string* sp2, sp3; // another way of pointer declaration, somehow misleading

	int ival1 = 1024;
	double dval1 = 1024.0;
	int *ip4 = &ival1; // pointer is initialized with the address of ival1
	int *ip5 = ip4; // avoid uninitialized pointers...
	int *ip6 = 0; // to do so zero initialization is a good idea if the object is not yet available
	int *ip7 = NULL; // the same as 0 - gets expanded my the preprocessor

	cout << "ip4: " << *ip4 << " ip5: " << *ip5 << " ip6: " << &ip6 << " ip7: " << &ip7 << endl;
	
	// void pointers can point to all types of objects - other pointers are bound to their type
	void *pv = &ival1;
	pv = &dval1;

	// const int i = 0; *ip = i;

	int iv1 = 1024, iv2 = 2048;
	int *pi = &iv1, *pi2 = &iv2;
	pi = pi2; // pi now points to ival2
	cout << "pi: " << *pi << " iv1: " << iv1 << endl;

	// Difference between refence and pointer
	int &ri = iv1, &ri2 = iv2;
	ri = ri2; // references do not change, but the value of the refence changes...
	cout << "ri: " << ri << " iv1: " << iv1 << endl;

	// pointer to pointers
	int **ppi = &pi;
	cout << "The value of iv1\n"
		 << "direct value: " << iv1 << "\n"
		 << "pointer value: " << *pi << "\n"
		 << "pointer of pointer value: " << **ppi << endl;

	// array automatically points to the first element
	int a[] = {1, 2, 42};
	int *pt = a; // points to a[0]
	cout << "Array-pointer: " << *pt << endl;

	// pointer arithmetic
	int *pt1 = pt + 1;
	cout << "Index 1 via pointer arithmetic: " << *pt1 << endl;

	// calculate pointer Difference
	ptrdiff_t delta = pt1 - pt;
	cout << "Delta: " << delta << endl;

	// arithmetic plus dereference
	cout << "Last value: " << *(pt + 2) << endl;
	cout << "Parantheses are essential: " << *pt + 2 << endl;

	// subscripts and pointers
	int *i = &a[1]; // points to the element with index 1
	int j = i[1]; // equivalent to *(i + 1)
	j = i[-1]; // equivalent to *(i - 1)

	// const pointer
	const double dbl = 42.0;
	const double *pdbl = &dbl; // a const pointer is needed to point to a const variable
	cout << *pdbl << endl;

	return 0;
}
