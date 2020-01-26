import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        clave = line.split('\t')[0]
        Letra = line.split('\t')[1]
        Letra = Letra.split(',')
        for i in Letra:
            sys.stdout.write("{},{}\n".format(i,clave))     