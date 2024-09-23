
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("Currently not implemented")
    
    def props_to_html(self):
        str_list = []
        for prop in self.props:
            str_list.append(f" {prop}=")
            str_list.append(f'"{self.props[prop]}"')
        joined_str = "".join(str_list)
        return(joined_str)
    
    def __repr__(self) -> str:
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"