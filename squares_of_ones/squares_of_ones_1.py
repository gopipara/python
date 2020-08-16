import argparse
from sys import argv

parser = argparse.ArgumentParser()
parser.add_argument('number_of_ones_to_square', type=int, nargs='?', default=9, help='Provide a number of ones to square. Ex: If you want to square 8 ones, provide 8')
args = parser.parse_args()

x=1
for counter, i in enumerate(range(1, int(args.number_of_ones_to_square)+1)):
     if (counter <=8):
          print(int(x)**2)
          x=str(x)+str(1)
