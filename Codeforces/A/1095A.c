#include<stdio.h>
main()
{
    int n,i,j;
    scanf("%d",&n);
    char a[n],s[n];
    scanf("%s",&a);
    for(i=0,j=0;i<n;j++,i=i+j)
    s[j]=a[i];
    for(i=0;i<j;i++)
    printf("%c",s[i]);
    
}
