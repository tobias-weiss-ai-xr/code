#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char const* argv[])
{
	char ch0[] = {'C', '+', '+'}; 		// no null, no C-style string
	char ch1[] = {'C', '+', '+', '\0'}; // explicit 0
	const char *cp1 = "C++"; 			// null termination added automatically
	const char *cp2 = "Python"; 			// null termination added automatically
	char *cp0 = ch0;					// points to the first element of an array but no C-style string
	char *cp3 = ch1;					// points to the first element of a 0-terminated (C-Style) char array

	cout << "strlen of cp1: " << strlen(cp1) << endl;
	cout << "strlen of cp2: " << strlen(cp2) << endl;
	cout << "strcmp of cp1 and cp2: " << strcmp(cp1, cp2) << endl;
	cout << "strcat of cp1: " << strcat(ch1, cp1) << endl;
	cout << "strncat of cp1: " << strncat(ch1, cp1, 2) << endl;
	char ch2[4]; 
	strcpy(ch2, ch1);
	cout << "ch2 after copy from ch1:" << ch2 << endl;

	return 0;
}
