import cs50

# count letters


def count_letters(text):
    n = 0
    for i in range(len(text)):
        if text[i].isalpha():
            n += 1
    return n

# count words


def count_words(text):
    n = 1
    for i in range(len(text)):
        if text[i] == ' ':
            n += 1
    return n

# count sentences


def count_sentences(text):
    n = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            n += 1
    return n
    

# read text
text = cs50.get_string("Text: ")

L = count_letters(text)
W = count_words(text)
S = count_sentences(text)
# Coleman-Liau index
ind = 0.0588 * (float(L) / W * 100) - 0.296 * (float(S) / W * 100) - 15.8
# output answers
if ind >= 16:
    print("Grade 16+")
elif ind < 1:
    print("Before Grade 1")
else:
    print("Grade {:0.0f}".format(ind))
