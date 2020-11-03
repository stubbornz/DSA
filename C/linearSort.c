#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
void linearSort(int *,int,int);
int main()
{
int *array,e,size,i;
printf("Enter size of Array: ");
scanf("%d",&size);
array=(int *)malloc(sizeof(int)*size);
printf("Enter elements of array to be sorted:\n");
for(e=0;e<=size-1;e++) 
{
scanf("%d",&i);
array[e]=i;
}
linearSort(arary,0,size-1);
printf("Sorted array:\n");
for(e=0;e<=size-1;e++) printf("%d\n",array[e]);
free(array);
return 0;
}
void linearSort(int *x,int lb,int ub)
{
int e,f,g;
e=lb;
while(e<=ub-1)
{
f=e+1;
while(f<=ub)
{
if(x[f]<x[e])
{
g=x[e];
x[e]=x[f];
x[f]=g;
}
f++;
}
e++;
}
}
