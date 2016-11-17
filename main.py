import urllib
import re

#url = raw_input("Please enter the URL to scrape: ")
lastId = raw_input("Please enter the numeric ID of the highest athletic ID: ")
sport = raw_input("Please enter the sport: ")

url = "http://pacifictigers.com/sports/m-wpolo/2016-17/roster"

def removeTabs(htmltext):
    newString = ""
    for c in htmltext:
        if (c == '\r') or (c == '\n') or (c == '\t'):
            pass
        else:
            newString+=c
    return newString

regex = 'title="Player\'s Bio">(.+?)</a>'
regex2 = '<td data-title="Pos." >(.+?)</td>' #will be an array of positions that corresponds to names
pattern = re.compile(regex)
pattern2 = re.compile(regex2)

htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

raw_html = removeTabs(htmltext)

with open("Raw_HTML.txt", "w") as file:
    file.write(raw_html)

names = re.findall(pattern,htmltext)
pos = re.findall(pattern2, raw_html)


def removeWhitespace(pos):
    newPos = []
    for position in pos:
        newPos.append(position.strip(' '))
    return newPos


pos = removeWhitespace(pos)

with open("Output.txt", "w") as text_file:
    for index, n in enumerate(names):
        insertStatement = "insert into athlete values(" + str(int(lastId)+index) + ", '" + n + "', '"+ sport + "', '" + pos[index]+"', 0.00);"
        text_file.write(insertStatement+"\n")