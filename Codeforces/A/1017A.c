#include<stdio.h>
main()
{
    int n,i,a,b,c,d,r=1;
    scanf("%d",&n);
    int m[n];
    for(i=0;i<n;i++)
    {
        scanf("%d%d%d%d",&a,&b,&c,&d);
        m[i]=a+b+c+d;
    }
    for(i=1;i<n;i++)
    {
        if(m[i]>m[0])
        r++;
    }
    printf("%d",r);
    
}
