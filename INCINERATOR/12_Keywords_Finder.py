def checkio(text, words):
    return text



print checkio("This is only a text example for task example.", "example") == "This is only a text <span>example</span> for task <span>example</span>."

print checkio("Python is a widely used high-level programming language.", "pyThoN") == "<span>Python</span> is a widely used high-level programming language."

print checkio("It is experiment for control groups with similar distributions.", "is im") == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."

print checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."

print checkio("Did you find anything?", "word space tree") == "Did you find anything?"

print checkio("Hello World! Or LOL", "hell world or lo") == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
