#include <iostream>
#include "Sales_item.h"

int main(){
	Sales_item total, trans;
	if (std::cin >> total) {
		while (std::cin >> trans) {
			if ( total.isbn() == trans.isbn()){
				// match: update the running total
				total = total + trans;
			} else {
				// no match: print & assign to total
				std::cout << total << std::endl;
				total = trans;
			}	
		}
		// remember to print last record
		std::cout << total << std::endl;
	} else {
		std::cout << "No data?" << std::endl;
		return -1; // indicate falure
	}	
	return 0;
}
