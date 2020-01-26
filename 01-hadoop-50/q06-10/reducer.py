import sys
if __name__ == '__main__':
    Letra = {}
    for line in sys.stdin:
        line = line.strip()
        k = line.split(',')[0]
        val = line.split(',')[1]
        val=float(val)
        if k in Letra.keys():
            Letra[k].append(val)
        else:
            Letra[k]=[]
            Letra[k].append(val)
    for k in Letra.keys():
        maxl =max(Letra[k])
        minl =min(Letra[k])
        sys.stdout.write("{}\t{}\t{}\n".format(k, maxl, minl))