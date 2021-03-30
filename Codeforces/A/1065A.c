#include<stdio.h>
main()
{
    int t,j;
    scanf("%d",&t);
    long long s,a,b,c,x=0;
    for(j=0;j<t;j++)
    {
        scanf("%lld%lld%lld%lld",&s,&a,&b,&c);
        x=s/c;
        x=x+(x/a)*b;
        printf("%lld\n",x);
        
    }
}
