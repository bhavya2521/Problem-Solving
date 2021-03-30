#include<stdio.h>
#include<string.h>
#define VOWEL (k=='a' || k=='e' || k=='i' || k=='o' || k=='u')
#define CONSO (k!='a' && k!='e' && k!='i' && k!='o' && k!='u')
main()
{
    int n,i,x=0;
    char s[100],k;
    scanf("%s",&s);
    n=strlen(s);
    if(n==1)
    {
        k=s[0];
        if(VOWEL || k=='n')
        printf("YES");
        else
        printf("NO");
    }
    else
    {
    for(i=0;i<n-1;i++)
    {
        k=s[i];
        if(CONSO && k!='n')
        {
            k=s[i+1];
            if(VOWEL)
            continue;
            else
            {
                x=1;
                break;
            }
        }        
    }
    k=s[n-1];
    if(CONSO && k!='n')
    x=1;
    if(x==0)
    printf("YES");
    else
    printf("NO");
    }
    
}
