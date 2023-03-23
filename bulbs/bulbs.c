#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;
//output
void print_bulb(int bit);
//transform ascii
string ascii(string msg);
//transform bin
void binary(string ascii, int z[][BITS_IN_BYTE], int n);


int main(void)
{
    // TODO
    string msg;

    msg = get_string("Message: ");
    //if empty msg return 0
    if (strlen(msg) == 0)
    {

        return 0;
    }
    //if msg not empty continu
    else
    {

        int n = strlen(msg);
        int z[n][BITS_IN_BYTE];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j <= 7; j++)
            {
                z[i][j] = 0;
            }
        }
        string asci = ascii(msg);
        binary(asci, z, n);
        for (int i = 0; i <= strlen(msg) - 1; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                print_bulb(z[i][j]);
            }
            printf("\n");
        }
    }
}

//transform binary
void binary(string ascii, int z[][BITS_IN_BYTE], int n)
{
    for (int i = 0; ascii[i] != '\0'; i++)
    {
        int h = ascii[i];
        while (h != 0)
        {
            for (int j = 0; j < 8; j++)
            {
                if (h % 2)
                {
                    z[i][7 - j] = 1;
                    h = h / 2;
                }
                else
                {
                    z[i][7 - j] = 0;
                    h = h / 2;
                }
            }
        }
    }
}
//trandsform ascii
string ascii(string msg)
{
    for (int i = 0; msg[i] != '\0'; i++)
    {
        msg[i] = (int)msg[i];

    }
    return msg;
}
//output
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}







