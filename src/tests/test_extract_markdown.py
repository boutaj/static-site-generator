import unittest

from functions.extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another one ![image2](https://i.imgur.com/rAn0m.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/rAn0m.png"),
            ],
            matches,
        )

    def test_extract_markdown_images_malformed(self):
        matches = extract_markdown_images(
            "This is text with an malformed ![image(https://i.imgur.com/zjjcJKZ.png)]"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a link [Click me](https://example.com)"
        )
        self.assertListEqual([("Click me", "https://example.com")], matches)

    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "This is a link [Click me](https://example.com) and this another one [Click me](https://notexample.com)"
        )
        self.assertListEqual(
            [
                ("Click me", "https://example.com"),
                ("Click me", "https://notexample.com"),
            ],
            matches,
        )

    def test_extract_markdown_malformed_link(self):
        matches = extract_markdown_links(
            "This is a link [Click me(https://example.com)"
        )
        self.assertListEqual([], matches)
