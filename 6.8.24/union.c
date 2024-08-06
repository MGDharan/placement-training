#include <stdio.h> 
union myUnion { 
	int intValue; 
	float floatValue; 
	char charValue; 
}; 
int main() 
{ 
	union myUnion u; 
	union myUnion* ptr = &u; 
	ptr->intValue = 100; 
	printf("The intValue is: %d\n", ptr->intValue);  
	ptr->floatValue = 3.14; 
	printf("The floatValue is: %f\n", ptr->floatValue); 

	return 0; 
}
