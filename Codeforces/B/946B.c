#include<stdio.h>
int main()
{
    long long n,m,x;
    scanf("%lld%lld",&n,&m);
    while(1)
    {
     if(n==0 || m==0)
		break;
	 if(n>=2*m)
		{
		n=n-(2*m);
		}
     else 
	   {
		if(m>=2*n)
		{
     	m=m-(2*n);
		}
		else 
		break;

       }
    }
    printf("%lld %lld",n,m);
return 0;
}