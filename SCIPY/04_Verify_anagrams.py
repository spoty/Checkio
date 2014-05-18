def make_dict(text):
    def count_char(text_structure, char):
        if char not in text_structure:
            text_structure[char] = {}
        (text_structure[char]) = text.count(char)
    text_structure = {}
    for char in text:
        count_char(text_structure, char)
    return text_structure

def checkio(text1, text2):
    """
    You are given two words or phrase. Verify If they are anagrams or not.
    Return True or False
    """
    # # Remove whitespaces and apply lowercases.
    clean = lambda text: text.lower().replace(' ','')
    return make_dict(clean(text1)) == make_dict(clean(text2))




print checkio("Programming", "Gram Ring Mop")
print checkio("Hello", "Ole Oh")
print checkio("Kyoto", "Tokyo")
