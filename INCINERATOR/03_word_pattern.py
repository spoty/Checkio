"""
Input: Two arguments. A pattern as a positive integer and a command as a string.

Output: Is the pattern coincide with the command or not as a boolean.

      42 == 00101010
12a0b3e4 == DDLDLDLD
--------------------
    True    VVVVVVVV

     101 == 01100101
ab23b4zz == LLDDLDLL
--------------------
   False    XVXVXXXV
"""


def check_command(c,w):
    c = [int(x) for x in bin(c)[2:].zfill(len(w))]
    w = map(lambda x: 0 if x in "0123456789" else 1,w)
    return True if c == w else False




print check_command(42, "12a0b3e4") == True
print check_command(101, "ab23b4zz") == False
