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

# XPath Expressions