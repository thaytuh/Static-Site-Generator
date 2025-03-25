


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # will be overridden by child class
    def to_html(self):
        raise NotImplementedError
    
    # represents the HTMl attributes of the node
    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    # prints node to see tag, value, children, props
    def __repr__(self):
        item = f"HTMLNode\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
        return item

# leaf node is an HTML node with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    # converts to html
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            props_html = ""
            if self.props:
                props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

# parent node is any other HTML node that is not a leaf node
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be None")
        if self.children is None:
            raise ValueError("Children cannot be None")
        # opening tag
        html = f"<{self.tag}"
        # if properties exist, add them
        if self.props:
            for prop, value in self.props.items():
                html += f' {prop}="{value}"'
        # close opening tag
        html += ">"
        # add children (recursion)
        for child in self.children:
            html += child.to_html()
        # add closing tag
        html += f"</{self.tag}>"
        return html

