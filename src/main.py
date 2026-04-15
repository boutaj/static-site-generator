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

print(LeafNode("p", "This is a paragraph of text.")) # "<p>This is a paragraph of text.</p>"
print(LeafNode("a", "Click me!", {"href": "https://www.google.com"})) # '<a href="https://www.google.com">Click me!</a>'


node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node.to_html())