#include<stdio.h>
#include<string.h>
int vowel(char k);
int main()
{
    int i,c=0;
    char a[1005],b[1005];
    scanf("%s%s",&a,&b);
    if(strlen(a)!=strlen(b))
    printf("NO");
    else
    {
        for(i=0;i<strlen(a);i++)
        {
            if(vowel(a[i])!=vowel(b[i]))
            {
                printf("NO");
                return 0;
            }
        }
        printf("YES");
    }
}
int vowel(char k)
{
    if(k=='a' || k=='e' || k=='i' || k=='o' || k=='u')
    return 1;
    else
    return 0;
}
