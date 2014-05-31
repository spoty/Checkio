from datetime import datetime
from string import maketrans
"""
Input:
    An unspecific time string (could be hh:mm:ss or h:m:s or hh:m:ss format,
    with no specific format)

Output:
    A string of Morse symbol from binary representation with specific format:
    "h h : m m : s s"
    where each digits represented as sequence of "." and "-"
"""

def checkio(t):
    cas=[bin(int(x))[2:] for x in
    ("{:%H:%M:%S}".format(datetime.strptime(t, "%H:%M:%S"))) if x != ':']

    binary=('%02d %04d : %03d %04d : %03d %04d' % (int(cas[0]), int(cas[1]),
    int(cas[2]), int(cas[3]), int(cas[4]), int(cas[5])))

    trans_table = maketrans("01", ".-")
    return binary.translate(trans_table)


print checkio( "10:37:49" )
print checkio( "21:34:56" )
print checkio( "00:1:02" )
print checkio( "23:59:59" )

# checkio=lambda data: __import__("re").sub(r"\d+",lambda match: " ".join(bin(
#     digit)[2:].zfill(4) for digit in divmod(int(match.group()),10)),data
#     ).replace(":0"," : ")

# print checkio("10:37:49")
