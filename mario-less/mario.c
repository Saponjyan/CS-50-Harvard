#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for Height
    int x;
    do
    {
        x = get_int("Height: ");
    }
    while (x > 8 || x < 1);

    //we go through the lines
    for (int i = 1; i <= x; i++)
    {
        //put spaces
        for (int j = x - i; j > 0; j--)
        {
            printf(" ");
        }
        // put #
        for (int p = 0; p < i; p++)
        {
            printf("#");
        }
        printf("\n");
    }


}