#include<stdio.h>
main()
{
    int t;
    long n,a,b,v,c;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%ld%ld%ld%ld",&n,&v,&a,&b);
        c=n/v-b/v+a/v;
		if(a%v==0)
		c--;
		printf("%ld\n",c);
    }
}
