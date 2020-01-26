import sys
if __name__ == '__main__':
    Letra = {}
    for line in sys.stdin:
        line = line.strip()
        k = line.split(',')[0]
        valor = line.split(',')[1]
        valor=float(valor)
        if k in Letra.keys():
            Letra[k].append(valor)
        else:
            Letra[k]=[]
            Letra[k].append(valor)
    for k in Letra.keys():
        suml =sum(Letra[k])
        avgl =suml/float(len(Letra[k]))
        sys.stdout.write("{}\t{}\t{}\n".format(k, suml, avgl))
