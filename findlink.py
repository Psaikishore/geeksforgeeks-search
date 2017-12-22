import BeautifulSoup
import lxml.html
import urllib2
url="http://www.geeksforgeeks.org"
url1="https://www.geeksforgeeks.org/"
newline='\n'
#i=1
def linkfind(finurl): #find all the links corresponding to ths
    r=correctlist(finurl)
    for link in r.xpath('//a/@href'):
        fh.write('\t')
        if(checklink(link)):
            fh.write(link.encode('utf8')+newline.encode('utf8'))

def checklink(finurl):
    #checks for the non required website links in the html pages
    if finurl==url1 or finurl=='/':
        return 0
    if '#' in finurl:
        return 0
    ignorelist=["quiz","youtube","linkedin","google","twitter","practice","tumblr","javascript","facebook","reddit",
    "microsoft","page","about","category","privacy-policy","licenses"]
    #must include category subheader later
    for i in ignorelist:
        if i in finurl:
                return 0
    return 1

def correctlist(finurl):
#to select the required elements of a page and to filter out the rest
#created readable buffer to cut out and the made it into lxml object for parsing
    page=urllib2.urlopen(finurl)
    dom=page.read()
    startloc=dom.find("strong");
    endloc=dom.rfind("disqus_thread")
    dom=dom[startloc:endloc]
    dom =  lxml.html.fromstring(dom)
    return dom

def createdictionary(url):
    '''
    page=urllib2.urlopen(url)
    dom=page.read()
    dom =  lxml.html.fromstring(dom)
    '''
    i=1
    dom=correctlist(url)

    linkdict={0:"https://geeksforgeeks.org"}
    fh=open("second.py","w")#open the file for topic dictionary
    #gh=open("test","w")#open file for values in in each topic

    fh.write("secondstage=")
    fh.close()
    for link in dom.xpath('//a/@href'):
        if(checklink(link)):
            newword={i:link}
            linkdict.update(newword)
            i=i+1
            finstr=link.encode('utf8')+newline.encode('utf8')#utf8 encoding to avoid errors (256 bit)
            '''
            linkfind(link)
            gh.write(finstr)
            gh.write('\n\n'+'->->->NEXT SITE' +link+'\n\n')
            #retain these lines to create initial createdictionary
            '''
    with open("second.py","a") as myfile:
        myfile.write(str(linkdict))
        myfile.close()



def openlink(url):
    dom=correctlist(url)
    for link in dom.xpath('//a/@href'):
        if(checklink(link)):
            with open("mu","a") as myfile:
                str1=link+'\n'
                myfile.write(str1)
                myfile.close()
