#include<stdio.h>
#include<stdlib.h>
int compare(int *p, int *q);
int main()
{
    int n,k,i,min,x,j;
    scanf("%d%d",&n,&k);
    long a[n];
    for(i=0;i<n;i++)
    scanf("%ld",&a[i]);
    qsort(a, n, sizeof(int), compare);
    if(a[k-1]==a[k] || a[k]==a[k-1]+1 || (k==0 && n==1 && a[0]==1))
    printf("-1");
    else if(k==0 && n==1 && a[0]!=1)
    printf("1");
    else if(k==0)
    printf("-1");
    else
    printf("%ld",a[k-1]);
    
}
int compare(int *p, int *q) {
    int x = *p;
    int y = *q;
    if (x < y)
        return -1;  
    else if (x > y)
        return 1;   

    return 0;
}