
import sys
low = []

low.append({'`':0, '1': 1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':10,'-':11,'=':12})
low.append({'Q':0,'W':1,'E':2,'R':3,'T':4,'Y':5,'U':6,'I':7,'O':8,'P':9,'[':10,']':11,'\\':12})
low.append({'A':0,'S':1,'D':2,'F':3,'G':4,'H':5,'J':6,'K':7,'L':8,';':9,"'":10})
low.append({'Z':0,'X':1,'C':2,'V':3,'B':4,'N':5,'M':6,',':7,'.':8,'/':9})

for line in sys.stdin:
    outstring= []
    for i in range(len(line)):
        if line[i] == " ":
            outstring.append(" ")
        for j in range(len(low)):
            if line[i] in low[j]:
                index = low[j][line[i]]
                index -= 1

                B = list(filter(lambda y : low[j][y] == index,list(low[j].keys())))

                outstring.append(B[0])

    print("".join(outstring))
