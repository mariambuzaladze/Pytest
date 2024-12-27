import math

def main():
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))

    print(f"You will need {calculate(length, width)} gallons of paint")

def calculate(l,w):
    return math.ceil(l*w/350)

if __name__=="__main__":
    main()
