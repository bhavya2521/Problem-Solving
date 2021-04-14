#include<stdio.h>
#include<string.h>
int main()
{
    int n,k,i,d,c=0,x;
    scanf("%d%d",&n,&k);
    long a;
	int b[10];
    while(n--)
    {
       
        for(i=0;i<10;i++)
		b[i]=0;
		x=0;
        scanf("%ld",&a);
       	while(a!=0)
		{
		d=a%10;
        b[d]++;
		a=a/10;
		}
        for(i=0;i<=k;i++)
        {	
            if(b[i]==0)
			{
            x=1;
            break;
            }
			
        }
        if(x==0)
        c++;
    }
    printf("%d",c);
    
}