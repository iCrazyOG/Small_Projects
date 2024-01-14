#include <iostream>

using namespace std;

void swap( int* first, int* second);

int main(){
    int x,y;
    cout << "enter a number: " << endl;
    cin >> x;
    cout << "enter a number: " << endl;
    cin >> y;

    int* ptr1= &x; 
    int* ptr2= &y;

    swap(ptr1,ptr2);

    cout << *ptr1 << " " << *ptr2;

    return 0;
}


void swap( int* first, int* second){
    int temp = *first;
    *first = *second;
    *second = temp;
}