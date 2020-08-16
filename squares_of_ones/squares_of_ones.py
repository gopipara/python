import argparse
from sys import argv

parser = argparse.ArgumentParser()
parser.add_argument('number_of_ones_to_square', type=int, nargs='?', default=9, help='Provide a number of ones to square. Ex: If you want to square 8 ones, provide 8')
args = parser.parse_args()

i, n = 1, int(args.number_of_ones_to_square)

def num_concat(num1, num2):
    # find number of digits in num2
     digits = len(str(num2))
     # add zeroes to the end of num1
     num1 = num1 * (10**digits)
     # add num2 to num1
     num1 += num2
     return num1

num_concat(1,8)
for counter, i in enumerate([i] * n):
    if counter == 0:
        print(i)
    elif ((counter >= 1) and (counter <=8)):
        output = num_concat(i, int((str([i] * counter)[1:-1]).replace(', ','')))
        print(output * output)
