#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
//include libs
// create a new type
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //check argc
    if (argc < 2)
    {
        printf("Usage: \n");
        return 1;
    }

    //open file
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        //cant open file
        printf("cant read file.\n");
        return 1;
    }
    //buffer size
    BYTE buffer[512];
    int nova = 0;
    FILE *img = NULL;
    char name[8];

    //fread
    while (fread(&buffer, 512, 1, input))
    {
        //read the file
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {

            if (nova > 0)
            {
                //close file
                fclose(img);
            }
            //write file
            sprintf(name, "%03i.jpg", nova);
            nova ++;
            img = fopen(name, "w");
        }
        if (nova > 0)
        {
            fwrite(&buffer, 512, 1, img);
        }
    }
    // close file
    fclose(input);
    fclose(img);

}