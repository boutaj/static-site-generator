from functions.extract_markdown import extract_markdown_images, extract_markdown_links
from functions.split_nodes import split_nodes_link
from nodes.htmleafnode import LeafNode
from nodes.htmlnode import HTMLNode
from nodes.textnode import TextNode, TextType

# print(TextNode("This is some anchor text", TextType.BOLD, "https://test.com"))

# span = HTMLNode("span", "Google", None, None)
# print(HTMLNode("a", None, span, {
#     "href": "https://www.google.com",
#     "target": "_blank",
# }))

# print(LeafNode("p", "This is a paragraph of text.")) # "<p>This is a paragraph of text.</p>"
# print(LeafNode("a", "Click me!", {"href": "https://www.google.com"})) # '<a href="https://www.google.com">Click me!</a>'


# """


# [
#                 TextNode("bold", TextType.BOLD),
#                 TextNode(" and ", TextType.TEXT),
#                 TextNode("italic", TextType.ITALIC),
#             ],

# """

# node = TextNode("**bold** and _italic_", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

# print(split_nodes_delimiter(new_nodes, "_", TextType.ITALIC))


# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

# print(extract_markdown_images(text))

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

print(new_nodes)
