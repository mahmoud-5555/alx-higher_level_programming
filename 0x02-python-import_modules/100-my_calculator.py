#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        opr = sys.argv[2]
        if opration == '+':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.add(a, b)))
        elif opration == '-':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.sub(a, b)))
        elif opration == '*':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.mul(a, b)))
        elif opration == '/':
            print("{} {} {} = {}".format(a, opr, b, calculator_1.div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    except genral Error:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
