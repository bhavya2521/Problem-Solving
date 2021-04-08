#include<stdio.h>
main()
{
    int n,i,c=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=1;i<n-1;i++)
    {
        if(a[i]==0 && a[i-1]==1 && a[i+1]==1)
        {
            a[i-1]=0;
            a[i+1]=0;
            c++;
        }
        
    }
    printf("%d",c);
}