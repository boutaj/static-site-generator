from nodes.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        def none_to_string(value):
            return value if value else ""
        return f"<{none_to_string(self.tag)}{self.props_to_html()}>{none_to_string(self.value)}{none_to_string(self.children)}</{none_to_string(self.tag)}>"
    def __repr__(self):
        return super().__repr__()