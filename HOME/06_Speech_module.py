numbers = "zero one two three four five six seven eight nine".split()
print numbers
numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen".split())
numbers.extend("seventeen eighteen nineteen".split())
numbers.extend(tens if ones == "zero" else (tens + " " + ones)
               for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split()
               for ones in numbers[0:10])

print numbers[42]
print numbers[99]
print numbers[10]

# import re
# text = "0 1 2 3 4 5 6 7 8 9".split()

# text.extend(

# tens if ones == 0 else (tens + ones)
# for tens in "1 2 3 4 5 6 7 8 9".split()
# for ones in text[0:10]

# )
# text.extend(

#     hundreds if tens == 0 else (ones + hundreds + tens)
#     for ones in text[0:10]
#     for hundreds in "1 2 3 4 5 6 7 8 9".split()
#     for tens in text[0:10]
#             )


# print text
