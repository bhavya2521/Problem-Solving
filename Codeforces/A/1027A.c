#include<stdio.h>
main()
{
    int n,t,i,x,y,c=0;
    scanf("%d",&t);
    while(t--)
    {
        c=0;
        scanf("%d",&n);
        char a[n];
        scanf("%s",&a);
        for(i=0;i<n/2;i++)
        {
         x=a[i],y=a[n-i-1];
         if(x==y|| x-y==2 || x-y==-2)
         continue;
         else
         {
             c=1;
             break;
         }
        }
        if(c==1)
        printf("NO\n");
        else
        printf("YES\n");
    }
}