#include <iostream>
#include <cmath>

//Area of a circle
int main(){
    double r;
    const double pi=3.14;

    using namespace std;
    cout << "Enter the radius: ";
    cin >> r;

    cout <<"The area is " <<pi*(pow(r,2));

    return 0;
}