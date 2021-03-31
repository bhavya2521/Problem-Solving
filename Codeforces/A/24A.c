#include<stdio.h>
main()
{
    long long int m,n,a,r,c;
    scanf("%I64d%I64d%I64d",&m,&n,&a);
    if(n%a==0)
    r=n/a;
    else
    r=n/a+1;
    if(m%a==0)
    c=m/a;
    else
    c=m/a+1;
    printf("%I64d",r*c);
}