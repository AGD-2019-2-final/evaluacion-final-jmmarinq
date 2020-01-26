import sys
if __name__ == "__main__":    
    for line in sys.stdin:
        pp = line.split(',')[3]
        a = line.split(',')[4]
        sys.stdout.write("{}\t{}\t\n".format(pp, a))