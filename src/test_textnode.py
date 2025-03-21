import unittest
import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_textnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


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

class TestMarkdowntoTextNode(unittest.TestCase):
    def test_code_onedelim(self):
        node = TextNode("This is text with a `code block` word", TextType.NormalText)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CodeText), [
    TextNode("This is text with a ", TextType.NormalText),
    TextNode("code block", TextType.CodeText),
    TextNode(" word", TextType.NormalText),
    ])
    
    def test_italic_twodelim(self):
        node = TextNode("This is _italic_ text with a _second_ italic block",TextType.NormalText)
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ItalicText), [
            TextNode("This is ", TextType.NormalText),
            TextNode("italic", TextType.ItalicText),
            TextNode(" text with a ", TextType.NormalText),
            TextNode("second", TextType.ItalicText),
            TextNode(" italic block", TextType.NormalText)
        ])
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)




if __name__ == "__main__":
    unittest.main()
