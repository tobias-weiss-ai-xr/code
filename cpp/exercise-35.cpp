#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::cin;
using std::endl;

int main(){
	string s1;
	string s2(s1);
	string s3("value");
	string s4(5, 'c');
	string s5(3, 'x');
	for(string::size_type ix = 0; ix <= s5.size()-1; ++ix){
		s5[ix] = '.';
	}
	cout << s5 << endl;
	
	string line;
	// print whole line
	// while (getline(cin, line)) {
	// print every word in a single line
	while (cin >> line) {
		cout << line << endl;
		cout << "The size is: " << line.size() << endl;
		if(line.size() == 1){
			cout << "The size is equal to 1." << endl;
		}
		if (line.empty()){
			// Case can not be reached!
			cout << "The line is empty." << endl;
		}
	}
	
	return 0;	
}
