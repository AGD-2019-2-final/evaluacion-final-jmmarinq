import sys
if __name__ == '__main__':
    pp1={}
    for line in sys.stdin:
        line = line.strip()
        pp = line.split('\t')[0]
        a = line.split('\t')[1]
        a=int(a)
        if pp in pp1.keys():
          pp1[pp].append(a)
        else:
          pp1[pp]=[]
          pp1[pp].append(a)
    for pp in pp1.keys():
        sump=max(pp1[pp])
        sys.stdout.write("{}\t{}\t\n".format(pp, sump))