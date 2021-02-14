#include <iostream>
#include <bitset>

using namespace std;

int main()
{
    unsigned char bits = 255;
    unsigned char ch_a = 'a';
    bitset<8> bs = bits;
    cout << "print char 255: " << bits << endl;
    cout << "print bitset 255: " << bs << endl;

    cout << "print char of a: " << ch_a << endl;
    cout << "print bitset of a: " << bitset<8>(ch_a) << endl;
    cout << "print char of 97:" << char(97) << endl;

    cout << "negated 255 as char: " << ~bits << endl; // carefull converts to signed
    unsigned char bits_negated = ~bits;
    cout << "negated 255 as char (cast explicit as unsigned): " << bits_negated << endl; // now explicitly casted
    cout << "negated 255 as bitset (cast explicit as unsigned): " << bitset<8>(bits_negated) << endl; // same binary value...
    cout << "negated 255 as char: " << bitset<8>(~bits) << endl;
    cout << "negated 255 as bitset: " << ~bs << endl;

    bits = '1';
    cout << "print bitset of '1': " << bitset<8>(bits) << endl;
    bits = bits << 1;
    cout << "left shift by 1: " << bits << endl;
    cout << "as bitset: " << bitset<8>(bits) << endl;

    bits = '1';
    bits = bits << 2;
    cout << "left shift by 2: " << bits << endl;
    cout << "as bitset: " << bitset<8>(bits) << endl;

    bits = '1';
    cout << "right shift by 1: " << (bits >> 1) << endl;
    cout << "as bitset: " << bitset<8>(bits >> 1) << endl;
    return 0;
}
