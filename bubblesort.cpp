//Largest value bubbles up to the end of the array
#include <iostream>

void bubblesort(int numbers[], int size){

    for (int i=0;i<size;i++){
        for (int j=0;j<size;j++){
            if (numbers[j] > numbers [j+1]){
                int temp = numbers[j];
                numbers[j]=numbers[j + 1];
                numbers[j + 1] =temp;
            }
        }
    }

    for (int a=0;a<size;a++){
        std::cout << numbers[a];
    }
    
}

int main(){
    int nums[]={4,8,5,1,0,6};

    using namespace std;
    int s=size(nums);
    bubblesort(nums,s);


    return 0;
}



