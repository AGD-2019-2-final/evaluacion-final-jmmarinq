import sys
if __name__ == '__main__':
    b=[]
    for line in sys.stdin:
        line = line.strip()
        line = line.split('\t')
        pp = line[0]
        a = line[1]
        a=int(a)
        b.append((pp,a))           
    b.sort(key=lambda b: b[1])
    for i in b:
       sys.stdout.write("{}\t\n".format((i[0] + "," + str(i[1]))))