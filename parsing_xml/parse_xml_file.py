import xml.etree.ElementTree as ET

# parse the file
tree = ET.parse('movies.xml')
root = tree.getroot()

print(root.tag) # collection
print(root.attrib) # {}

# iterate over sub-elements
for child in root:
    print(child.tag, child.attrib)
    # element to whole document
    print(ET.tostring(child, encoding='utf8').decode('utf8'))

# element to whole document
# print(ET.tostring(root, encoding='utf8').decode('utf8'))

# search with tag
for movie in root.iter('movie'):
    print(movie.attrib.get("title"))

print("-"*100)
# print the content of a tag
for movie in root.iter('movie'):
    print(movie.attrib.get("title"))
    for description in movie.iter("description"):
        print(description.text)
    print("-"*50)

# check if an element is in a tag
print([elem.tag for elem in root.iter("movie")])

if not [elem.tag for elem in root.iter("movieesd")]:
    print("movieesd is not present")

# XPath Expressions
# findall() on element text
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)
# findall on element attribute
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
# to return the parent element of the current element
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)

# Modifying an XML