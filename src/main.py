from textnode import TextNode, TextType


def main():
    test_obj = TextNode("this is some anchor text", TextType.LINK, "https://localhost:8888")
    print(test_obj)


main()