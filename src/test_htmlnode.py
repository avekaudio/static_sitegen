import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
       testnode = HTMLNode(props={"href": "https://www.google.com",
    "target": "_blank",})
       self.assertEqual(testnode.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props2(self):
        testnode = HTMLNode(props={"p": "This is a paragraph", "img": "Funny cat pic"})
        self.assertEqual(testnode.props_to_html(), ' p="This is a paragraph" img="Funny cat pic"')

    def test_props3(self):
        testnode = HTMLNode(props={"h1": "This is a header", "href": "https://boot.dev", "p": "paragraph oh yeah"})
        self.assertEqual(testnode.props_to_html(), ' h1="This is a header" href="https://boot.dev" p="paragraph oh yeah"')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    
    def test_leaf_to_html_a_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class TestParentNOde(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    
        

    
if __name__ == "__main__":
    unittest.main()