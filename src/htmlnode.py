class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented Error")
    
    def props_to_html(self):
        html = ""
        if self.props is None:
            return ""
        for tag, value in self.props.items():
            html += f" {tag}=\"{value}\""
        return html
    
    def __repr__(self):
        def none_to_string(value):
            return value if value else ""
        return f"<{none_to_string(self.tag)}{self.props_to_html()}>{none_to_string(self.value)}{none_to_string(self.children)}</{none_to_string(self.tag)}>"
    