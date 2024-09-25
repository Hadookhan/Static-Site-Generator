
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
        if self.props == None or isinstance(self.props, dict) == False:
            return ""
        for prop in self.props:
            str_list.append(f" {prop}=")
            str_list.append(f'"{self.props[prop]}"')
        joined_str = "".join(str_list)
        return(joined_str)
    
    def __repr__(self) -> str:
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,value, tag=None, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value must contain data")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __setitem__(self, key, value):
        raise Exception("Cannot add children to a LeafNode")
    
class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, "", children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be specified")
        if not self.children:
            raise ValueError("Children must be specified")
        
        # Start with the opening tag
        result = f"<{self.tag}>"
        
        # Process all children
        for child in self.children:
            if hasattr(child, "to_html"):
                result += child.to_html()
            else:
                result += str(child)
        
        # Close the tag
        result += f"</{self.tag}>"
        
        return result
        
        