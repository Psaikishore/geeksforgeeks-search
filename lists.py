'''
functions made for listing the contents and diplaying them
'''
from mydict import linkdict
def list1():
    f1=open("mu","w")
    for i in linkdict:
        if(i>1):
            s=linkdict[i]
            finstr=str(i)+' '+s+'\n'
            f1.write(finstr)
    f1.write("\n\n\n")
    f1.write("\n-----------------------------------------------NEXT OPTIONS----------------------------------------\n")
    f1.close()
def adress(n):
    return linkdict[n]
def list2():
    url="https://www.geeksforgeeks.org/"
    from second import secondstage
    with open("mu","a") as f1:
        for i in secondstage:
            if(i>1):
                s=secondstage[i]
                s=s[len(url):]
                finstr=str(i)+' '+s+'\n'
                f1.write(finstr)
        f1.write("\n\n\n")
        f1.write("\n\n")
        f1.close()
def adress2(n):
    from second import secondstage
    return secondstage[n]
