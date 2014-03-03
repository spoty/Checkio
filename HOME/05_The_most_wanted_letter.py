import collections
import re

text = "Lorem ipsum dolor sit amet!!!!!!!!!!"


def checkio(text):
    text2 = re.sub('[ \t, !]', '', text)
    x = sorted(collections.Counter(text2).most_common(1))[0][0]
    y = x.lower()
    return y


print checkio(text)
