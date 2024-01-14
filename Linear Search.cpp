#include <iostream>

using namespace std;

int find (int numbers[],size_t size, int target){

    for (int i=0;i<size;i++){
        if (numbers[i]==target);
            return i;
    }

    return -1;
}
int main() {
    int nums[]={1,2,3,4,5};
    int target;
    cout << "Enter a number to search for: " << endl;
    cin >> target;

    cout << find(nums,size(nums),target);

    return 0;
}