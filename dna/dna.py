import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("ERROR")
        sys.exit(1)
    # TODO: Read database file into a variable
    df = []
    file1 = sys.argv[1]
    with open(file1) as f1:
        reader = csv.DictReader(f1)
        for c in reader:
            df.append(c)

    # TODO: Read DNA sequence file into a variable
    file2 = sys.argv[2]
    with open(file2) as f2:
        dnk = f2.read()

    # keys
    k = {}
    keys = []
    for i in df[0].keys():
        keys.append(i)

    # TODO: Find longest match of each STR in DNA sequence
    for i in range(1, len(keys)):
        k[keys[i]] = longest_match(dnk, keys[i])

    # TODO: Check database for matching profiles
    for d in range(len(df)):
        count = 0
        for d2 in k.keys():
            if int(k[d2]) == int(df[d][d2]):
                count += 1
                if count == len(k):
                    print(df[d]["name"])
                    return
    else:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
