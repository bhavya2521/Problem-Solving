#include<stdio.h>
main()
{
    int n;
    scanf("%d",&n);
    if(n==1)
    printf("-1");
    else
    printf("%d 2",n-n%2);
}
