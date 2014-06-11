"""
Input: Two arguments. A rhyme as a string and a word as a string (lowercase).
Output: The coordinates of the word.

Coordinates: [row_start, column_start, row_end, column_end],
where
    row_start:
         is the line number for the first letter of the word.
    column_start
        is the column number for the first letter of the word.
    row_end
        is the line number for the last letter of the word
    column_end
        is the line number for the last letter of the word.

    Counting of the rows and columns start from 1.
"""


def checkio(rhyme, word):
    poem = [x.replace(" ", "") for x in rhyme.split("\n")]

    for coo_r, x in enumerate(poem):
            for coo_w,z in enumerate(x):
                if x[coo_w] == word[0]:
                    if x[coo_w:coo_w+len(word)] == word:
                        return [coo_r+1, coo_w+1, coo_r+1, coo_w+len(word)]
    # print "\n".join(rhyme)



print checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]

# print checkio("""He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""", "noir") == [2, 14, 2, 16]
