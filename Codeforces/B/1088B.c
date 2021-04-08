#include<stdio.h>
#include<stdlib.h>
int compare(int *p, int *q);
int main()
{
    int n,k,i,j,d=1,x,s=0;
    scanf("%d%d",&n,&k);
    long a[n],min,b[n];
    for(i=0;i<n;i++)
    scanf("%ld",&a[i]);
    qsort(a, n, sizeof(int), compare);
	b[0]=a[0];
	for(i=1;i<n;i++)
	{
		if(a[i]!=a[i-1])
		{
		b[d]=a[i];
		d++;
		}
	}
	
	printf("%ld\n",b[0]);
    for(i=1;i<k;i++)
    {
       if(i<d)
	   {
		s=s+b[i-1];
		b[i]=b[i]-s;
        printf("%ld\n",b[i]);
       }
       else 
       printf("%d\n",0);
    }
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