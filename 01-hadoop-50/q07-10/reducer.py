import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == '__main__':

    for line in sys.stdin:
        clave,valor_format,fecha,valor = line.split("\t")
        valor=int(valor)
        
        sys.stdout.write("{}   {}   {}\n".format(clave, fecha, valor))