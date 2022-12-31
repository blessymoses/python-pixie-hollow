import re
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

print("-"*100)

# Modifying an XML
for movie in root.iter('movie'):
    print(movie.attrib)

# find the element by attribute value
a_movie = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(a_movie)

print(a_movie.attrib)
a_movie.attrib["title"]= "My new title"
print(a_movie.attrib)

tree.write("new_movies.xml")

print("-"*100)

new_tree = ET.parse("new_movies.xml")
new_root = new_tree.getroot()
for movie in new_root.iter("movie"):
    print(movie.attrib)

print("-"*100)

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
    # search for the commas in the format text
    match = re.search(",", form.text)
    if match:
        form.set("multiple", "Yes")
    else:
        form.set("multiple", "No")

tree.write("new_movies.xml")

new_tree = ET.parse("new_movies.xml")
new_root = new_tree.getroot()
print("-"*100)
for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

print("-"*100)

# to view the tree structure
print(ET.tostring(root, encoding='utf8').decode('utf8'))