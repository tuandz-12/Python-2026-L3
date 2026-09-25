#Ex8
def exact_even(n):
    n = [1,4,5,-1,10]
    result = []
    for number in n:
        if number % 2 == 0:
            result.append(number)
    return result
number = [1,4,5,-1,10]
input(exact_even(number))