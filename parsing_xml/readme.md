# Parsing XML using Python ElementTree

## What is XML?
- XML documents have sections, called elements, defined by a beginning and an ending tag. 
  - A `tag` is a markup construct that begins with < and ends with >. 
  - The characters between the start-tag and end-tag, if there are any, are the element's content. 
  - Elements can contain markup, including other elements, which are called "child elements".
- The largest, top-level element is called the `root`, which contains all other elements.
- `Attributes` are name–value pair that exist within a start-tag or empty-element tag. 
  - An XML attribute can only have a single value.
  - Each attribute can appear at most once on each element.

## ElementTree
- Python's built in library, `ElementTree`, has functions to read and manipulate XMLs.

## XPath expressions
- XPath is a query language used to search through an XML quickly and easily. 
- XPath stands for XML Path Language and uses, as the name suggests, a "path like" syntax to identify and navigate nodes in an XML document.
### findall()
- `findall()` function traverses the immediate children of the referenced element.
- The function .findall() always begins at the element specified. 
- This type of function is extremely powerful for a "find and replace". 
- You can even search on attributes!
- use '...' inside of XPath to return the parent element of the current element.

