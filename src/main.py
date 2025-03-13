from textnode import TextType, TextNode
def main():
    node = TextNode("dummytext", TextType.Links, "https://www.boot.dev")
    print(node)

main()