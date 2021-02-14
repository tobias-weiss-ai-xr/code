#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::ispunct;

int main(void)
{
	string s("Hello World!");
	string::size_type punc_cnt = 0;

	// count punctuation characters in s
	for (string::size_type index = 0; index < s.size(); ++index){
		if(ispunct(s[index]))
			++punc_cnt;
	}
	cout << "There is " << punc_cnt << " punctuation characters in " << s << endl;

	// Convert all characters to lower
	for (string::size_type index = 0; index < s.size(); ++index){
		s[index] = std::tolower(s[index]);
	}
	cout << "Only lower chars: " << s << endl;
	return 0;
}
