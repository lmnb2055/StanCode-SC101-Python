"""
File: class_reviews.py
Name:Sidney
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

Exit = '-1'

def main():
    """
    TODO:
    """
    s = input('Which class? ')
    s = s.upper()
    num1 = 0
    num2 = 0
    if s == Exit:
        print('no class scores were entered. ')
    else:
        if s == 'SC001':
            score1 = int(input('Score: '))
            num1 += 1
            total1 = score1
            max1 = score1
            min1 = score1
        elif s == 'SC101':
            score2 = int(input('Score: '))
            num2 += 1
            total2 = score2
            max2 = score2
            min2 = score2
        while True:
            if s == 'SC001' and num1 == 0:
                score1 = int(input('Score: '))
                num1 += 1
                total1 = score1
                max1 = score1
                min1 = score1
            elif s == 'SC101' and num2 == 0:
                score2 = int(input('Score: '))
                num2 += 1
                total2 = score2
                max2 = score2
                min2 = score2

            s = input('Which class? ')
            s = s.upper()
            if s == 'SC001' and num1 != 0:
                score1 = int(input('Score: '))
                num1 += 1
                total1 += score1
                if max1 < score1:
                    max1 = score1
                if min1 > score1:
                    min1 = score1

            elif s == 'SC101' and num2 != 0:
                score2 = int(input('Score: '))
                num2 += 1
                total2 += score2
                if max2 < score2:
                    max2 = score2
                if min2 > score2:
                    min2 = score2

            if s == Exit:
                if num1 == 0:
                    print('=============SC001=============')
                    print('No score for SC001.')
                else:
                    avg1 = float(total1 / num1)
                    print('=============SC001=============')
                    print('MAX(001): ' + str(max1))
                    print('MIN(001): ' + str(min1))
                    print('AVG(001): ' + str(avg1))

                if num2 == 0:
                    print('=============SC101=============')
                    print('No score for SC101.')
                else:
                    avg2 = float(total2 / num2)
                    print('=============SC101=============')
                    print('MAX(101): ' + str(max2))
                    print('MIN(101): ' + str(min2))
                    print('AVG(101): ' + str(avg2))
                break









# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
