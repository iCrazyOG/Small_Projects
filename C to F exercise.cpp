#include <iostream>
//Program to convert c to f
int main(){
    double celcius;

    using namespace std;
    cout <<"Enter the temperature in Celcius:"<<endl;
    cin >>celcius;

    cout <<"The temperature is " <<(celcius*9/5)+32 <<" Farenhite";


    return 0;
}