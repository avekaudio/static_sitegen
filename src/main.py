from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():
    node = TextNode("dummytext", TextType.Links, "https://www.boot.dev")
    print(node)

main()