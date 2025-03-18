from enum import Enum
from htmlnode import *

class TextType(Enum):
    NormalText = "normal"
    BoldText = "bold"
    ItalicText = "italic"
    CodeText = "code"
    Links = "links"
    Images = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return (
            self.text == node.text 
            and self.text_type == node.text_type 
            and self.url == node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.NormalText:
              return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BoldText:
              return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ItalicText:
              return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CodeText:
              return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.Links:
            return LeafNode("a", text_node.text, props={"href": text_node.url,})
        if text_node.text_type == TextType.Images:
              return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text},)
        else: 
              raise Exception("Invalid text type")
        
              

