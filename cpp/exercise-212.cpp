#include <iostream>

/* Calculate m^n */
int main(){
	char _;
	_ = 'x';
	//bool catch-22;
	//char 1_or_2 = '1';
	float Float = 3.14f;	

	std::cout << _ << std::endl;
	std::cout << "Base?" << std::endl;
	int base = 0;
	int power = 0;
	std::cin >> base;
	std::cout << "Power?" << std::endl;
	std::cin >> power;
	int result = base;
	for ( int i = 1; i < power; i++ ){
		std::cout << i << ": " << result << std::endl;
		result *= base;	
	}
	std::cout << "Result: " << result << std::endl;
}
