#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// count letters
int count_letters(string text);
// count words
int count_words(string text);
// count sentences
int count_sentences(string text);

int main(void)
{
    // read text
    string text = get_string("Text: ");
    int L = count_letters(text);
    int W = count_words(text);
    int S = count_sentences(text);

    // printf("%s\n%i letters\n%i words\n%i sentences\n",text,L,W,S);
    float ind = 0.0588 * ((float)L / W * 100) - 0.296 * ((float)S / W * 100) - 15.8;
    //output answers
    if (ind >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (ind < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %0.0f\n", ind);
    }


}
// count letters
int count_letters(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            n += 1;
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            n += 1;
        }

    }
    return n;

}
// count words
int count_words(string text)
{
    int n = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            n += 1;
        }

    }
    return n;

}
// count sentences
int count_sentences(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            n += 1;
        }
    }
    return n;

}