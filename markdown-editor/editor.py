import sys
import os
from parser import parse, STYLE

arguments = sys.argv

if len(arguments) == 1:
    print("Markdown Editor: No arguments passed.")
    exit(1)

i = 1
ispreview = False
preview = None
isexport = False
export = None

while i < len(arguments):
    argument = arguments[i]
    if argument == "--preview" or argument == "-p":
        ispreview = True
        preview = "index.html"
    elif argument == "--export" or argument == "-et":
        isexport = True
        export = "file.pdf"
    else:
        path = argument
    i+=1

try:
    with open(path,"r",encoding="utf-8") as file:
        data = file.read()
except:
    print("File not found")
    exit(1)

lines = data.split("\n")
template = ["<!DOCTYPE html>","<html>","<head>","<title>Document</title>","</head>",f'<body style="{STYLE["body"]}">',"BODY","</body>","</html>"]

if not ispreview:
    for i,line in enumerate(lines):
        print(line)
else:
    i = 0
    body = parse(lines)
    html = "\n".join(template)
    html = html.replace("BODY",body)
    with open("index.html","w") as file:
        file.write(html)