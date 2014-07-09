def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        number = "Fizz Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    else:
        number = "The number"
    return str(number)

print checkio(2)


# getValue=lambda key:{'blah':1,'foo':2,'bar',3}.get(key,4)
# exec{'key1':'code','key2':'code'}[key]+';codeThatWillAlwaysExecute'

#+{(False, False):'Fizz Buzz',(False, True):'Fizz',(True, False):'Buzz',(True, True):str(number)}[fizz_buzz]

# number = 5
# d = {(False, False):'Fizz Buzz',(False, True):'Fizz',(True, False):'Buzz',(True, True):str(number)}
# exec'fizz_buzz = bool(number % 3), bool(number % 5);print d[fizz_buzz]'

