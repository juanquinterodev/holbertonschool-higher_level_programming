#!usr/bin/python3
def print_last_digit(number):
    if number < 0:
        dig = (number * -1) % 10
    else:
        dig = number % 10

        print("{}".format(dig), end="")
        return dig
