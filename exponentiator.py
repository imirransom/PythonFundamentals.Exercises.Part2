def exponentiate(num1, num2):
    return num1**num2

def raise_to_the_fourth_power(num3):
    return exponentiate(num3, 4)

raise_to_the_fourth_power(exponentiate(3, 6))

square = lambda x: exponentiate(x, 2)

cube = lambda x: exponentiate(x, 3)


