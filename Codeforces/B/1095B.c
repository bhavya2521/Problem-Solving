#include<stdio.h>
int check(int a[ ],int n);
int main()
{
    int n,i;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("%d",check(a,n));
return 0;
}
int check(int a[ ],int n)
{
    int i,max1=a[0],max2,min1=a[0],min2;
    for(i=1;i<n;i++)
    {
        if(a[i]>max1)
        	{
            	max2=max1;
            	max1=a[i];
        	}
        else if(a[i]>max2)
        		max2=a[i];
        if(a[i]<min1)
            {
                min2=min1;
                min1=a[i];
            }
        	else if(a[i]<min2)
        		min2=a[i];
    }
    if((max1-min2)>(max2-min1))
    return (max2-min1);
    else
    return (max1-min2);
}