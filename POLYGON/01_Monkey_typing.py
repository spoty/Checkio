def count_words(text, words):
    return sum(1 for w in set(words) if w in text.lower())




print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
# count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2

