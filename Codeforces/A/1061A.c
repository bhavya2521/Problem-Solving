#include<stdio.h>
main()
{
    long long n,c,s=0;
    scanf("%lld%lld",&n,&c);
    s=c/n;
    if(c%n!=0)
    s++;
    printf("%lld",s);
}
    
