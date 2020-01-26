import sys
if __name__ == '__main__':
    minimo = []
    orden = []
    for line in sys.stdin:
        la = line.split(',')[0]
        da = line.split(',')[1]
        va = line.split(',')[2]
        va = int(va)
        orden.append((la,da,va))
        orden.sort(key=lambda b: (b[2]))
    n = len(orden)
    for i in range(6):
        minimo.append(orden[i])
    for la,da,va in minimo:
        sys.stdout.write("{}\t{}\t{}\n".format(la,da,va))