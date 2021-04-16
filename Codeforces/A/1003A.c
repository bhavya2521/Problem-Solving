#include<stdio.h>
int coin(int a[ ],int n);
int main()
{
    int n,i;
    scanf("%d",&n);
    if(n==1)
    printf("1");
    else
    {
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    printf("%d",coin(a,n));
    }
}
int coin(int a[ ],int n)
{
    int i,max;
	int b[100]={0};
    for(i=0;i<n;i++)
        b[a[i]-1]++;
	max=b[0];
	for(i=1;i<100;i++)
	{
		if(b[i]>max)
		max=b[i];
	}
return max;
}