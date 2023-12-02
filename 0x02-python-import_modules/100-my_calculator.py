#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    mahmoud = {'+' : calculator_1.add}
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        opr = sys.argv[2]
        if opr == '+':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.add(a, b)))
        elif opr == '-':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.sub(a, b)))
        elif opr == '*':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.mul(a, b)))
        elif opr == '/':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    except IndexError:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    