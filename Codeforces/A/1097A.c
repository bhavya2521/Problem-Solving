#include<stdio.h>
main()
{
    int i,s=0;
    char a[2],b[2];
    scanf("%s",&a);
    for(i=0;i<5;i++)
        {
            scanf("%s",&b);
            if(a[0]==b[0] || a[1]==b[1])
            {
                s=1;
                break;
            }
        }
        if(s==0)
        printf("NO");
        else
        printf("YES");
}
