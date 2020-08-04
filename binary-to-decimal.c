#include <stdio.h>
#include <math.h>

int main()
{
    int b[100],n,i,r,q,j,x,y,z;

    printf("Binary: ");
    scanf("%d",&n);

    for(i=0;n>0;i++)
    {
        r = n%10;
        b[i] = r;
        q = n/10;
        n = q;
    }


    x = 0;
    for(j=0;j<=100;j++)
    {
        y = b[j]*pow(2,j);
        if(y >= 0 && y < 10000)
        {
            z = x + y;
            x = z;
        }
        else
        {
            break;
        }

    }

    printf("%d",x);

    return 0;
}
