import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        Letra = line.split('   ')[0]
        val = line.split('   ')[2]
        sys.stdout.write("{},{}\n".format(Letra, val))
