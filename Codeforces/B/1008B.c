#include<stdio.h>
int cmp(long a[ ],long b[ ],long i);
int main()
{
    int n,i;
    scanf("%d",&n);
    long a[n],b[n];
    for(i=0;i<n;i++)
    scanf("%ld%ld",&a[i],&b[i]);
    if(a[0]>b[0])
    b[0]=a[0];
    for(i=1;i<n;i++)
    {
        if((cmp(a,b,i)==0))
        {
         printf("NO");
         return 0;
        }
    }
    printf("YES");
    return 0;
}
int cmp(long a[ ],long b[ ],long i)
{
    int t;
    if(a[i]<=b[i-1] && b[i]<b[i-1])
    {
    if(a[i]>b[i])
     b[i]=a[i];
    return 1;
    }
    else if(b[i]<=b[i-1])
    return 1;
    else if(a[i]<=b[i-1])
    {
    b[i]=a[i];
    return 1;
    }
    else 
    return 0;
}