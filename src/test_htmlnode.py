import unittest
from htmlnode import HTMLNode

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
        

    
if __name__ == "__main__":
    unittest.main()