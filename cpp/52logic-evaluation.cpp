#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s("Espressions in C++ are composed...");
    string::iterator it = s.begin();
    // convert first work in s to uppercase
    while (it != s.end() && !isspace(*it)) {
        *it = toupper(*it);
        ++it;
    }
    cout << s << endl;

    // 5.7
    char *ch = "Hello World!";
    int i = 0;
    while (ch && *ch && i != 10) {
        cout << ch << " " << i << endl;
        ++i;
    }

    // 5.8
    while(i != 42){
        cout << "Please enter a digit. 42 to exit: " << endl;
        cin >> i;
    }

    // 5.9
    int a = 1;
    int b = 2;
    int c = 3;
    int d = 4;
    if(b > a && c > b && d > c)
        cout << "great!" << endl;

    return 0;
}
