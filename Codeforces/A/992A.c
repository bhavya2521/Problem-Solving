#include<stdio.h>
#include<stdlib.h>
int compare(int *p, int *q);
int main()
{
    int n,i,d=2;
    scanf("%d",&n);
    long a[n],min,b[n];
    for(i=0;i<n;i++)
    scanf("%ld",&a[i]);
    qsort(a, n, sizeof(int), compare);
	i=0;
	while(a[i]==0)
	i++;
	b[1]=a[i];
	for(;i<n;i++)
	{
		if(a[i]!=a[i-1] && a[i]!=0)
		{
		b[d]=a[i];
		d++;
		}
	}
	printf("%d",d-2);
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