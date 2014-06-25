def checkio(number):
    ans, digit  = '', 9
    while digit > 1:
        if number%digit != 0:
            digit -= 1
        else:
            ans = str(digit) + ans
            number /= digit
    return int(ans) if number == 1 else 0


print checkio(25)
