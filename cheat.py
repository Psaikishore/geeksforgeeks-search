import urllib2
from lxml import html
from mydict import linkdict
import findlink
import lists
def stripTags(pageContents):
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("Output:")
    pageContents = pageContents[startLoc:endLoc]
    inside = 0
    text = ''
    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text
fh=open("mu","w")
url="http://geeksforgeeks.org"
lists.list1()

print "available content succesfully printed to the file name 'mu' pls select option:"
m=input()
print "your content will be displayed shorly in the above file"
searchtext=lists.adress(m);

finalurl1=url+'/'+searchtext
print(finalurl1)
findlink.createdictionary(finalurl1)

lists.list2()#display second set of lists
print "select the program to be loaded"
m=input()
from second import secondstage
finalurl1=secondstage[m]
'''
the above 3 lines are to be rethought of
'''

page=urllib2.urlopen(finalurl1)
html=page.read()
text=stripTags(html)
with open("mu","a") as myfile:
    myfile.write(text)
    myfile.close()
fh.close()

'''
&#8220; = "(left)
&#8221; = ""(right)
&#8217= '(aporstophe)
&#92;=\
&#48=0
&quot;=""
'''
