#include<stdio.h>
main()
{
    long long n,k,a,b,c,s;
    scanf("%lld%lld",&n,&k);
    a=2*n,b=5*n;c=8*n;
    s=a/k+b/k+c/k;
    if(c%k!=0)
    s++;
    if(b%k!=0)
    s++;
    if(a%k!=0)
    s++;
    printf("%lld",s);
    
}
