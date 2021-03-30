#include<stdio.h>
#include<math.h>
main()
{
    int t,j;
    scanf("%d",&t);
    long long n,x,y,d,c,c1,c2;
    for(j=0;j<t;j++)
    {
        c=0,c1=0,c2=0;
        scanf("%lld%lld%lld%lld",&n,&x,&y,&d);
        if(abs(x-y)%d==0)
        c=abs(x-y)/d;
        else
        {
            if((y-1)%d==0)
            {
                c1=((x-1)/d)+(y-1)/d;
                if((x-1)%d!=0)
                c1++;
            }
            if((n-y)%d==0)
            {
                c2=((n-x)/d)+(n-y)/d;
                if((n-x)%d!=0)
                c2++;
            }
            if(c1!=0 && c2==0)
            c=c1;
            else if(c1==0 && c2!=0)
            c=c2;
            else if(c1!=0 && c2!=0)
            {
                if(c1>c2)
                c=c2;
                else
                c=c1;
            }
            else
            c=-1;
            
        }
        printf("%lld\n",c);
    }
}
