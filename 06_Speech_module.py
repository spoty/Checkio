numbers = "zero one two three four five six seven eight nine".split()
print numbers
numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen".split())
numbers.extend("seventeen eighteen nineteen".split())
numbers.extend(tens if ones == "zero" else (tens + " " + ones) 
    for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split()
    for ones in numbers[0:10])




print numbers[42]
print numbers[99]
print numbers
    