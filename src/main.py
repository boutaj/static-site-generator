import os
import shutil
import sys

from functions.markdown_to_blocks import markdown_to_html_node


class Copy:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def dir(self):
        if os.path.exists(self.destination):
            shutil.rmtree(self.destination)
        os.makedirs(self.destination, exist_ok=True)
        self.files(self.source, self.destination)

    def files(self, current_source, current_destination):
        for entry in os.listdir(current_source):
            source_path = os.path.join(current_source, entry)
            destination_path = os.path.join(current_destination, entry)

            if os.path.isfile(source_path):
                shutil.copy(source_path, destination_path)
                print(f"Copied file: {source_path} -> {destination_path}")
            else:
                os.makedirs(destination_path, exist_ok=True)
                self.files(source_path, destination_path)


def extract_title(markdown):
    for line in markdown.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("# ") and not stripped_line.startswith("##"):
            return stripped_line[2:].strip()
    raise Exception("no h1 header found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    with open(from_path, encoding="utf-8") as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, encoding="utf-8") as template_file:
        template = template_file.read()

    content_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", content_html
    )
    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(page_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                dest_html_path = os.path.splitext(dest_path)[0] + ".html"
                generate_page(source_path, template_path, dest_html_path, basepath)
            continue

        generate_pages_recursive(source_path, template_path, dest_path, basepath)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    Copy("static", "docs").dir()
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
