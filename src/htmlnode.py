


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
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    # prints node to see tag, value, children, props
    def __repr__(self):
        item = f"HTMLNode\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
        return item
