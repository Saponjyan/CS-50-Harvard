#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    for (int j = 0; j < candidate_count; j++)
    {
        if (strcmp(candidates[j].name, name) == 0)
        {
            candidates[j].votes += 1;
            return true;

        }



    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    string best;
    int b = 0;
    for (int n = 0; n <= candidate_count; n++)
    {
        if (b < candidates[n].votes)
        {
            b = candidates[n].votes;
            best = candidates[n].name;

        }

        //printf("%s %i\n",candidates[n].name,candidates[n].votes);
    }
    printf("%s\n", best);
    for (int n2 = 0; n2 <= candidate_count; n2++)
    {
        if (b == candidates[n2].votes && strcmp(candidates[n2].name, best) != 0)
        {

            printf("%s\n", candidates[n2].name);
        }

    }

    return;
}