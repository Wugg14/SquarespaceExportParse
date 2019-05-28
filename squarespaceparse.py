from xml.dom.minidom import parse
import xml.dom.minidom, re

#Regex combiling to remove HTML tags and spaces
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  removeSpaces = re.sub('&nbsp;', ' ', cleantext)
  return removeSpaces

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("SquarespaceExport.xml")
collection = DOMTree.documentElement

# Get all the Pages
pages = collection.getElementsByTagName("item")

endHTML = "<head></head><body>"
# Print detail of each page and concatenate to the HTML string 
for page in pages:
    
    title = page.getElementsByTagName('title')[0]
    titleData = title.childNodes[0].data
    endHTML +=  "<h1>Page Title: " + titleData + "</h1>"
    print("Title: %s" % titleData)
    content = page.getElementsByTagName('content:encoded')[0]
    contentData = content.childNodes[0].data
    cleanedData = cleanhtml(contentData)
    endHTML += "<p>" + cleanedData +"</p><hr />"
    print("Content: %s" % cleanedData)

#close the body tag before writing the HTML document
endHTML += "</body>"

with open("export.html", "w") as file:
    file.write(endHTML)
