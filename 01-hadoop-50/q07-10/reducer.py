import sys
import operator
from operator import itemgetter
if __name__ == '__main__':   
    for line in sys.stdin:
        codigo,letraa, fechaa, valora = line.split(",")
        valora = int(valora)
        sys.stdout.write("{}\t{}\t{}\n".format(letraa,fechaa,valora))