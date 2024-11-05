class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ''
        if self.props != None:
            for key in self.props:
                html += f' {key}="{self.props[key]}"'
        return html
    
    def __repr__(self):
        return (f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})')
        

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None, children=None):
        if children is not None:
            raise ValueError("LeafNode cannot have children")
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
        if self.tag == None or self.tag == '':
            return f'{self.value}'
        else:
            if self.props == None or self.props == {}:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                properties = self.props_to_html()
                return f'<{self.tag}{properties}>{self.value}</{self.tag}>'



class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None, value=None):
        if value is not None:
            raise ValueError('ParentNode cannot have value')
        if children is None or children == []:
            raise ValueError('ParentNode must have children')
        if tag is None or tag == '':
            raise ValueError('ParentNode must have a tag')
        super().__init__(tag=tag, children=children, props=props, value=None)

    def to_html(self):
        final_str = ''
        for item in self.children:
            if type(item) == LeafNode:
                final_str += LeafNode.to_html(item)
            if type(item) == ParentNode:
                final_str += ParentNode.to_html(item)
        if self.props is None or self.props == {}:
            final_str = f'<{self.tag}>' + final_str + f'</{self.tag}>'
            return final_str
        else:
            properties = self.props_to_html()
            final_str = f'<{self.tag}{properties}>' + final_str + f'</{self.tag}>'
            return final_str


