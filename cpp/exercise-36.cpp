#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string s1, s2;

	cout << "Enter first string: ";	
	cin >> s1;
	cout << endl;

	cout << "Enter second string: ";
	cin >> s2;
	cout << endl;

	if (s1 == s2)
		cout << "The strings are equal!" << endl;
	else if(s1 < s2)
		cout << s1 << " is recognized less than " << s2 << endl;
	else
		cout << s2 << " is recognized less than " << s1 << endl;

	if (s1.size() == s2.size())
		cout << "The strings have the same length." << endl;
	else if (s1.size() < s2.size())
		cout << s1 << " is shorter than " << s2 << endl;
	else
		cout << s2 << " is shorter than " << s1 << endl;
	
	return 0;
}
