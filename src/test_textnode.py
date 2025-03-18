import unittest

from textnode import TextNode, TextType


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

    def text_node_to_html_node(text_node):
        

if __name__ == "__main__":
    unittest.main()
