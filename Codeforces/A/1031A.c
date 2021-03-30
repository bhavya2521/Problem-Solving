#include<stdio.h>
main()
{
    int w,h,k,i,s=0;
    scanf("%d%d%d",&w,&h,&k);
    for(i=1;i<=k;i++)
    {
        s=s+2*w+2*h-4;
        w=w-4,h=h-4;
        
    }
    printf("%d",s);
    
}
