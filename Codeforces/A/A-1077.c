#include<stdio.h>
main()
{
int t,i;
long long a,b,n;
scanf("%d",&t);
long long s[t];
for(i=0;i<t;i++)
{
scanf("%lld %lld %lld",&a,&b,&n);
s[i]=-b*(n/2)+a*(n-(n/2));
}
for(i=0;i<t;i++)
printf("%lld\n",s[i]);
}

