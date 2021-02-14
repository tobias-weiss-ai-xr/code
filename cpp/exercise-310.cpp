#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const* argv[])
{
	string text;
	cout << "Please enter string with punctuation: " << endl;
	cin >> text;
	for (string::size_type index = 0; index < text.size(); index++) {
		if (ispunct(text[index]))
			text[index] = ' ';
	}
	cout << text << endl;

	return 0;
}
