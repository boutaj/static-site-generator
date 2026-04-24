import os
import tempfile
import unittest

from main import extract_title, generate_page, generate_pages_recursive


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_strips_whitespace(self):
        markdown = "   # Hello Tolkien   "
        self.assertEqual(extract_title(markdown), "Hello Tolkien")

    def test_extract_title_raises_without_h1(self):
        markdown = "## Not an h1"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_generate_page(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            from_path = os.path.join(tmp_dir, "index.md")
            template_path = os.path.join(tmp_dir, "template.html")
            dest_dir = os.path.join(tmp_dir, "public")
            dest_path = os.path.join(dest_dir, "index.html")

            with open(from_path, "w", encoding="utf-8") as markdown_file:
                markdown_file.write("# Hello\n\nThis is a **test**.")

            with open(template_path, "w", encoding="utf-8") as template_file:
                template_file.write(
                    "<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>"
                )

            generate_page(from_path, template_path, dest_path, "/")

            with open(dest_path, encoding="utf-8") as generated_file:
                html = generated_file.read()

            self.assertEqual(
                html,
                "<html><head><title>Hello</title></head><body><div><h1>Hello</h1><p>This is a <b>test</b>.</p></div></body></html>",
            )

    def test_generate_page_rewrites_root_paths_with_basepath(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            from_path = os.path.join(tmp_dir, "index.md")
            template_path = os.path.join(tmp_dir, "template.html")
            dest_path = os.path.join(tmp_dir, "index.html")

            with open(from_path, "w", encoding="utf-8") as markdown_file:
                markdown_file.write("# Hello\n\n[Link](/contact)\n\n![Image](/images/pic.png)")

            with open(template_path, "w", encoding="utf-8") as template_file:
                template_file.write(
                    "<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>"
                )

            generate_page(from_path, template_path, dest_path, "/static-site-generator/")

            with open(dest_path, encoding="utf-8") as generated_file:
                html = generated_file.read()

            self.assertIn('href="/static-site-generator/contact"', html)
            self.assertIn('src="/static-site-generator/images/pic.png"', html)

    def test_generate_pages_recursive(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            content_dir = os.path.join(tmp_dir, "content")
            blog_dir = os.path.join(content_dir, "blog")
            template_path = os.path.join(tmp_dir, "template.html")
            public_dir = os.path.join(tmp_dir, "public")

            os.makedirs(blog_dir, exist_ok=True)

            with open(os.path.join(content_dir, "index.md"), "w", encoding="utf-8") as f:
                f.write("# Home\n\nWelcome home.")

            with open(os.path.join(blog_dir, "post.md"), "w", encoding="utf-8") as f:
                f.write("# Blog Post\n\nA _nested_ page.")

            with open(template_path, "w", encoding="utf-8") as f:
                f.write(
                    "<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>"
                )

            generate_pages_recursive(content_dir, template_path, public_dir, "/")

            with open(os.path.join(public_dir, "index.html"), encoding="utf-8") as f:
                home_html = f.read()

            with open(
                os.path.join(public_dir, "blog", "post.html"), encoding="utf-8"
            ) as f:
                post_html = f.read()

            self.assertEqual(
                home_html,
                "<html><head><title>Home</title></head><body><div><h1>Home</h1><p>Welcome home.</p></div></body></html>",
            )
            self.assertEqual(
                post_html,
                "<html><head><title>Blog Post</title></head><body><div><h1>Blog Post</h1><p>A <i>nested</i> page.</p></div></body></html>",
            )


if __name__ == "__main__":
    unittest.main()
