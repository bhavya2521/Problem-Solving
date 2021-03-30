#include<stdio.h>
main()
{
    long long n,a,b;
    scanf("%lld%lld%lld",&n,&a,&b);
    if(a+b<=n+1)
    printf("White");
    else
    printf("Black");
}
