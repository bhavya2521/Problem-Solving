#include<stdio.h>
#include<string.h>
main()
{
    int n1,n2,i,j,c;
    char a[200005],b[200005];
    scanf("%s%s",&a,&b);
    n1=strlen(a);
    n2=strlen(b);
    for(i=n1-1,j=n2-1,c=0;i>=0 && j>=0;i--,j--)
    {
        if(a[i]==b[j])
        c++;
        else
        break;
    }
    printf("%d",n1+n2-2*c);
    
}