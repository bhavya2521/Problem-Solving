#include<stdio.h>
main()
{
    long long int m,n,a;
    scanf("%I64d%I64d%I64d",&m,&n,&a);
    if(n%a==0)
    n=n/a;
    else
    n=n/a+1;
    if(m%a==0)
    m=m/a;
    else
    m=m/a+1;
    printf("%I64d",m*n);
}
