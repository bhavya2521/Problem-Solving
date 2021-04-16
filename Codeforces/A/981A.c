#include<stdio.h>
#include<string.h>
int palin(char a[ ],int n);
int main()
{
int n,i;
char a[100];
scanf("%s",&a);
n=strlen(a);
if(palin(a,n)==1)
printf("%d",n);
else
{
    for(i=1;i<n;i++)
        {
            if(a[0]!=a[i])
              {
                  printf("%d",n-1);
                  return 0;
              }
        }
    printf("0");
    
          
}

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