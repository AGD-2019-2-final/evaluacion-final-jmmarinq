import sys
if __name__ == "__main__":
    for line in sys.stdin:
        letra = line.split('   ')[0]
        fecha = line.split('   ')[1]
        valor = line.split('   ')[2]
        valor = int(valor)
        sys.stdout.write("{},{},{},{}\n".format(letra + str(valor/100), letra, fecha, valor))