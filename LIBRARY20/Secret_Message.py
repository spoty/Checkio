def find_message(m):
    return ''.join(l for l in m if l.isupper())



find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""
