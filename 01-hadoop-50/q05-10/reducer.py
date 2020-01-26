import sys
if __name__ == '__main__':
    meses = {}
    for line in sys.stdin:
        line = line.strip()
        k = line.split(',')[0]
        conta = line.split(',')[1]
        conta=int(conta)
        if k in meses.keys():
            meses[k].append(conta)
        else:
            meses[k]=[]
            meses[k].append(conta)
    for k in meses.keys():
        suml =sum(meses[k])
        sys.stdout.write("{}\t{}\n".format(k, suml))
