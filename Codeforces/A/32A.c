#include<stdio.h>
main()
{
    int n,i,j,c=0;
    long d;
    scanf("%d%ld",&n,&d);
    long a[n];
    for(i=0;i<n;i++)
    scanf("%ld",&a[i]);
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(abs(a[i]-a[j])<=d)
            c=c+2;
        }
    }
    printf("%d",c);

}
