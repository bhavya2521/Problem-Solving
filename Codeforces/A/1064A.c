#include<stdio.h>
#define TRI (c<a+b)
main()
{
    int a,b,c,t,s=0;
    scanf("%d%d%d",&a,&b,&c);
    if(a>c && a>b)
    t=c,c=a,a=t;
    else if(b>c && b>a)
    t=c,c=b,b=t;
    if(!TRI)
    printf("%d",c-a-b+1);
    else
    printf("0");
    
}

