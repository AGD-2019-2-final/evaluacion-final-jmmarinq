import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        if len(line) >=2:
            credito = line[2]
            sys.stdout.write("{}\t1\n".format(credito))