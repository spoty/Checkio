def checkio(words):
    list_ow = []
    for word in words.split():
        if word.isdigit():
            del list_ow[:]
        if word.isalpha():
            list_ow.append(word)
            if len(list_ow) >= 3:
                return True
    if len(list_ow) < 3:
        return False


print checkio("He is is 123 man")
