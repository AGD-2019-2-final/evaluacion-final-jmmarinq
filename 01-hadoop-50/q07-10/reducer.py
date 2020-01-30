import sys
if __name__ == '__main__':   
    for line in sys.stdin:
        concat,key,date,val= line.split("\t")
        val=int(val)
        sys.stdout.write("{}   {}   {}\n".format(key,date ,val))