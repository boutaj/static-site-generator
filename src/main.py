from functions.split_nodes_delimiter import split_nodes_delimiter
from nodes.htmleafnode import LeafNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, TextType
from nodes.htmlnode import HTMLNode


print(TextNode("This is some anchor text", TextType.BOLD, "https://test.com"))

span = HTMLNode("span", "Google", None, None)
print(HTMLNode("a", None, span, {
    "href": "https://www.google.com",
    "target": "_blank",
}))

# print(LeafNode("p", "This is a paragraph of text.")) # "<p>This is a paragraph of text.</p>"
# print(LeafNode("a", "Click me!", {"href": "https://www.google.com"})) # '<a href="https://www.google.com">Click me!</a>'


"""


[
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],

"""

node = TextNode("**bold** and _italic_", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

print(split_nodes_delimiter(new_nodes, "_", TextType.ITALIC))
