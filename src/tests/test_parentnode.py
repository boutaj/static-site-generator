import unittest

from nodes.htmleafnode import LeafNode
from nodes.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Hello"),
                LeafNode("span", "world"),
            ],
        )
        self.assertEqual(node.to_html(), "<div><p>Hello</p><span>world</span></div>")

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "container"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container"><p>Hello</p></div>',
        )

    def test_to_html_raises_when_tag_is_missing(self):
        node = ParentNode(None, [LeafNode("p", "Hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raises_when_children_are_missing(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
