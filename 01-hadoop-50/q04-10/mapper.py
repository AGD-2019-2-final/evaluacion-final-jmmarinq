import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        Letra = line.split('   ')[0]
        conta = 1
        sys.stdout.write("{},{}\n".format(Letra, conta))
        
