from __future__ import division
import math
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    magnitude = 0
    while abs(number) >= base and magnitude < len(powers)-1:
        magnitude += 1
        number /= base
    if decimals == 0:
        if number < 0: number = float("-"+str(math.floor(abs(number))))
        else: number = math.floor(number)
    return "{0:.{1}f}{2}{3}".format(number, decimals, powers[magnitude], suffix)



print friendly_number(255000000000, powers=["","k","M"])
# print friendly_number(-150, base=100, powers=["","d","D"])

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert friendly_number(102) == '102', '102'
#     assert friendly_number(10240) == '10k', '10k'
#     assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
#     assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
#     assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
