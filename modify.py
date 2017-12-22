'''
made for hash function and removing the tag "geeksforgeeks.org"

'''
from mydict import linkdict
'''
def hash(s,m):
    length=len(s)/4
    add=0
    for j in range length:
        c=s[j*4:j*4+4]
        mult=1
        for k in range len(c):
            add=add+c[k]*mult
            mult=mult*256
    return add%m
    the above hash is for removing duplicates, try it later in phase 2
'''
w={0:" "}
for i in range(len(linkdict)):
    if(i>=1):
        s=linkdict[i]
        startloc=s.find('g/')+2
        s=s[startloc:]
        #print s
        w1={i:s}
        w.update(w1)
fh=open("test","w")
fh.write(str(w))
fh.close()
