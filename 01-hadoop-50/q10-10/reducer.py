import sys
if __name__ == '__main__':
    Letra={}
    for line in sys.stdin:
        line = line.strip()
        clave = line.split(',')[0]
        a = line.split(',')[1]
        a = int(a)
        if clave in Letra.keys():
          Letra[clave].append(a)
        else:
          Letra[clave]=[]
          Letra[clave].append(a)
    for clave, valor in Letra.items():
        valor = sorted(valor, key=lambda x: x)
        valor = str(valor)[1:-1]
        valor = valor.replace(", ", ",")
        sys.stdout.write("{}\t{}\n".format(clave, valor))