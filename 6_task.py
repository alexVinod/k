fh_i=open('students.txt','r')
fh_o=open('output.txt','w')
lineCount=0
for line in fh_i:
    lineCount+=1
    line=line.strip()
    if lineCount==1:
        fh_o.write(line+"\tTotal")
    else:
        words=line.split()
        marks=words[1:]
        b=list(map(lambda x:int(x),marks))
        total=str(sum(b))
        final_line=line+'\t'+total
        fh_o.write(final_line)
    fh_o.write('\n')
        

fh_i.close()
fh_o.close()
