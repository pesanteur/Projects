"""Description from karan/Projects:
    Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found."""
VOWELS = ['a', 'e', 'i', 'o', 'u']

def count_vowels(word):
    count = 0
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0

    for i in word:
        i = i.lower()
        if i in VOWELS:
            count += 1
            if i == 'a':
                a_count += 1
            elif i == 'e':
                e_count += 1
            elif i == 'i':
                i_count += 1
            elif i == 'o':
                o_count += 1
            else:
                u_count += 1
        breakdown = 'This word/sentence contains %s a\'s, %s e\'s, %s i\'s, %s o\'s, and %s u\'s.' % (a_count, e_count, i_count, o_count, u_count)
    return count, breakdown
