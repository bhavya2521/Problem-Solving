
 #include<stdio.h>
#include<string.h>
int changes(char a[ ],int n);
main()
{
    int c;
    char a[15];
    scanf("%s",&a);
    c=changes(a,strlen(a));
    if(c==1 || (c==0 && strlen(a)%2!=0))
    printf("YES");
    else
    printf("NO");
}
int changes(char a[ ],int n)
{
    int i,c=0;
    for(i=0;i<n/2;i++)
    {
        if(a[i]==a[n-1-i]);
        else
        c++;
    }
    return c;
}
