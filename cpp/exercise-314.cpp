#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char const* argv[])
{
	vector<string> text;
	cout << "Please enter a text longer than eight words (exit with -1):" << endl;
	string tmp;
	while (cin >> tmp){
		text.push_back(tmp);
		if (tmp == "-1") {
			break;
		}
	}
	for (vector<string>::size_type ix = 0; ix != text.size()-1; ix++) {
		cout << text[ix];
		if((ix != 0) && (ix % 7 == 0))
			cout << endl;
	}
	cout << endl;
	return 0;
}
