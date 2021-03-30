#include<stdio.h>
main()
{
int y,b,r;
scanf("%d%d%d",&y,&b,&r);
for(;r>0;r--)
{
if(r-1<=b && r-2<=y)
{
printf("%d",3*r-3);
break;
}
}
}
