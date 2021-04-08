#include<stdio.h>
#include<string.h>
int palin(char a[ ],int n);
int main()
{
    char a[1005],c;
    int t,n,k,i;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",&a);
        n=strlen(a);
        if(palin(a,n)==0)
        {
          k=0;
          for(i=0;i<n-1;i++)
          {
              if(a[i]!=a[i+1])
              {
                c=a[i];
                a[i]=a[i+1];
                a[i+1]=c;
                printf("%s",a);
                k=1;
                break;
              }
          }
          if(k==0)
          printf("-1");
        }
        else
        printf("%s",a);
        printf("\n");
    }
    return 0;
}
int palin(char a[ ],int n)
{
    int i;
    for(i=0;i<n/2;i++)
    {
        if(a[i]!=a[n-1-i])
        return 1;
    }
    return 0;
}