import unittest

from nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            "a",
            "Google",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode("p", "hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
