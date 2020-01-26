import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        if len(line) >=2:
            pp = line[0]
            a = line[1]
            sys.stdout.write("{}\t{}\t\n".format(pp, a))