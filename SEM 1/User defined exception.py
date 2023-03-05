import sys
class illegalNoOfArguments(Exception):
    pass
class InvalidOperatorException(Exception):
    pass
class NegativeResultException(Exception):
    pass
try:
    if len(sys.argv) > 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        operator = sys.argv[3]
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            raise InvalidOperatorException
        if result >= 0:
            print(result)
        else:
            raise NegativeResultException
    else:
        raise illegalNoOfArguments
except illegalNoOfArguments:
    print("please enter 3 inputs")
except InvalidOperatorException:
    print("Plaese enter valid arithmatic operator")
except NegativeResultException:
    print("Result is negative")
except ZeroDivisionError:
    print("Cannot divide number by 0")
