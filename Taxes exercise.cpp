#include <iostream>
//Show the sales, state tax and county tax
int main(){
    int sales=95000;
    double state_tax=0.04*sales, county_tax=0.02*sales;

    using namespace std;
    cout <<"The total sales is $"<< sales<< endl<<"The state tax is $"
         <<state_tax <<endl <<"The county tax is $" <<county_tax <<endl
         << "Hence the total tax paid is $" <<state_tax+county_tax <<endl;

    return 0;
}