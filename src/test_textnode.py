import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BoldText)
        node2 = TextNode("This is a text node", TextType.BoldText)
        self.assertEqual(node, node2)

    def test_urldiff(self):
        node = TextNode("This is a text blob", TextType.Links, "https://youtube.com")
        node2 = TextNode("This is a text blob", TextType.Links)
        self.assertNotEqual(node, node2)

    def test_ttnoteq(self):
        node = TextNode("This is text", TextType.Images, "https://youtube.com")
        node2 = TextNode("This is text", TextType.CodeText, "https://youtube.com")
        self.assertNotEqual(node, node2)

class TestConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NormalText)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Google", TextType.Links, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "https://google.com",})
    
    def test_img(self):
        node = TextNode("This is an image", TextType.Images, "https://youtube.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://youtube.com", "alt": "This is an image"})


if __name__ == "__main__":
    unittest.main()
