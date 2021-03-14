#include <iostream>

#include "libtest/libtest.h"

int main()
{
	int x = 5;
	while(x > 0)
	{
		x--;
	}
	std::cout << "test" << std::endl;
	libtest();
	return(0);
}
