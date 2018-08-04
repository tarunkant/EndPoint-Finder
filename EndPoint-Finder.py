import re
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",
                        help="Input a URL i.e. https, http, ftp, etc..")
parser.add_argument("-f","--file",
                        help="Input file location")
parser.add_argument("-o","--output",
                        help="Output file location")
parser.add_argument("-c","--cookie",
                        help="Add URL cookie, in the form \"PHPSESSID=qw32312313\"")
args = parser.parse_args()

if(args.file!=None or args.url!=None):
    print """
.___     ..__         ,      .___      .
[__ ._  _|[__) _ *._ -+- ___ [__ *._  _| _ ._.
[___[ )(_]|   (_)|[ ) |      |   |[ )(_](/,[

            author: $_SpyD3r_$
 """
else:
    print parser.print_help()
    exit()

if(args.file):
    f = open(args.file,'r').read()
    content1 = f.split('"')
if(args.url):
    url=args.url
    if(args.cookie):
        cookie = args.cookie.split("=")
        req=requests.get(url,cookies={cookie[0]:cookie[1]})
        content1=req.text.split('"')
    else:
        req=requests.get(url)
        content1=req.text.split('"')

end_point = []
extension=(".png",".jpg",".wav",".jpeg",".json",".js",".php",".xml")    #more can be added, as requirement
start = ("/","http://","https://","file://","php://","ftp://","./","../")

def end_points(content):
    for i in content:
        if re.match("^[a-zA-Z0-9_\/:&?%.\-=]*$", i):
            if (i.startswith(start) or i.endswith(extension)):
                end_point.append(i)


    for i in content:
        if re.match("^[a-zA-Z0-9_\/:&?%.\-=]*$", i):
            if (not i.startswith(start)):
                temp = i.split("/")
                if "/"+temp[0] in end_point or "./"+temp[0] in end_point or "../"+temp[0] in end_point:
                    end_point.append(i)

def saving_in_file(end_point):
        f=open(args.output,'a')
        f.write(end_point)
        f.write("\n")

def print_end_points(end_point):
    start1=("http://","https://","file://","php://","ftp://")
    a="\n-----------------Remote files which are added-----------------------------------\n"
    if(args.output): saving_in_file(a)
    print a
    for i in end_point:
        if i.startswith(start1):
            print i
            if(args.output): saving_in_file(i)

    b="\n-----------------These files are present in server------------------------------\n"
    print b
    if(args.output): saving_in_file(b)
    for i in end_point:
        if i.endswith(extension):
            print i
            if(args.output): saving_in_file(i)

    c="\n-----------------These are files and directory, you can look into---------------\n"
    print c
    if(args.output): saving_in_file(c)
    start1=("/","./","../")
    for i in end_point:
        if i.startswith(start1) and not (i.endswith(extension)):
            print i
            if(args.output): saving_in_file(i)


    print "\n-----------------These directory can be present (not sure!!)--------------------\n"
    for i in end_point:
        if(not i.startswith(start) and not i.endswith(extension)):
            print i
            if(args.output): saving_in_file(i)


if __name__=='__main__':
    end_points(content1)
    end_point = set(end_point)
    print_end_points(end_point)
