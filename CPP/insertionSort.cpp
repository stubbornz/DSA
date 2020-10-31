#include <bits/stdc++.h> 
using namespace std; 

void insertionSort(int array[], int n) 
{ 
	int i,j,key; 
	for (i = 1; i < n; i++) 
	{ 
		key = array[i]; 
		j = i - 1; 

		/* Move elements of arr[0..i-1], that are 
		greater than key, to one position ahead 
		of their current position */
		while (j >= 0 && array[j] > key) 
		{ 
			array[j + 1] = array[j]; 
			j = j - 1; 
		} 
		array[j + 1] = key; 
	} 
} 

int main() 
{ 
    int size=0;
    cout<<"Enter no. of elements: ";
    cin>>size;
	int *array = new int[size]; 
    cout<<"Enter elements of array:"<<endl;
	for(int i=0;i<size;++i) cin>>array[i];
	insertionSort(array, size); 
    cout<<"Sorted array:"<<endl;
	for(int i=0;i<size;++i) cout<<array[i]<<endl;
	 
     return 0; 
} 


