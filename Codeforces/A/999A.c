#include<stdio.h>
main()
{
    int n,k,i,c=0,j;
    scanf("%d%d",&n,&k);
    int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]<=k)
        c++;
        else 
        break;
    }
    for(j=n-1;j>i;j--)
    {
        if(a[j]<=k)
        c++;
        else
        break;
    }
    printf("%d",c);
    
}
