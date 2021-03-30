#include<stdio.h>
main()
{
    int w,n,a,b,h1,h2,i;
    scanf("%d%d%d%d%d%d",&w,&n,&a,&h1,&b,&h2);
    for(i=0;i<n;i++)
    {
        w=w+n-i;
        if(n-i==h1)
            w=w-a;
        else if(n-i==h2)
            w=w-b;
        if(w<0)
        w=0;
        
    }
    printf("%d",w);
}


