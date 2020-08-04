#include <stdio.h>

int main()
{
    int B[100],n,i,j;

    printf("Number: ");
    scanf("%d",&n);

    i = 0;
    while(n>=1)
    {
        B[i] = n%2;
        n = n/2;
        i++;
    }
    for(j=i-1;j>=0;j--)
    {
        printf("%d",B[j]);
    }

    printf("\n");

    return 0;
}
