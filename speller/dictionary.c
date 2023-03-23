// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"
#include <cs50.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int siz = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    char tolow[LENGTH + 1];
    int j = 0;
    while (word[j] != '\0')
    {
        tolow[j] = tolower(word[j]);
        j++;
    }
    tolow[j] = '\0';

    node *new = table[hash(tolow)];

    while (new != NULL)
    {
        if (strcmp(new->word, tolow) == 0)
        {
            return true;
        }
        else
        {
            new = new->next;
        }

    }
    return false;

}

// Hashes word to a number
// unsigned int hash(const char *word)
// {
//     // TODO: Improve this hash function
//     return toupper(word[0]) - 'A';
// }

unsigned int hash(const char *word)
{
    unsigned int hash = 4096;
    for (int i = 0 ; word[i] != '\0' ; i++)
    {
        hash = 33 * hash + word[i];
    }
    return hash % N;
}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char w[LENGTH + 1];
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return false;
    }
    while (fscanf(f, "%s", w) != EOF)
    {
        siz++;
        node *new = malloc(sizeof(node));
        if (new == NULL)
        {
            unload();
            return false;
        }
        strcpy(new->word, w);
        unsigned int h = hash(w);
        if (table[h] == NULL)
        {

            table[h] = new;
            new->next = NULL;
        }
        else
        {
            node *g = table[h];
            new->next = g->next;
            g->next = new;
        }

    }
    fclose(f);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return siz;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *d = table[i];
            table[i] = table[i] -> next;
            free(d);
        }

    }
    return true;
}
