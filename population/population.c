#include <cs50.h>
#include <stdio.h>

int main(void)
{

    // TODO: Prompt for start size
    int n;
    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);//9

    // TODO: Prompt for end size

    int y;
    do
    {
        y = get_int("End size: ");
    }
    while (y < n);//10


    // TODO: Calculate number of years until we reach threshold

    int i = 0;
    if (y == n)
    {
        printf("Years: %i\n", i);
    }
    else
    {
        do
        {
            n += (int)(n / 3) - (int)(n / 4);
            i++;
        }
        while (n < y);

        // TODO: Print number of years
        printf("Years: %i\n", i);
    }
}
