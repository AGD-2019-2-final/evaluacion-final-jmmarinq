import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        meses = line.split('   ')[1]
        meses = line.split('-')[1]
        conta = 1
        sys.stdout.write("{},{}\n".format(meses, conta))