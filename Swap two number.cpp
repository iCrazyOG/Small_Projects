#include <iostream>

int main(){
    int a=1;
    int b=2;

    int temp=a;
    a=b;
    b=temp; //swap the values of variables 'a' and 'b'.
    std::cout << "The value of variable 'a' is: "<< a;
    std::cout << "\nThe value of variable 'b' is: "<< b;


    return 0;
}