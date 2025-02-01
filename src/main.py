from textnode import TextType, TextNode

print("hello world")

def main():
    dummy_node = TextNode("This is a dummy node", TextType.NORMAL, "https://www.boot.dev")
    print(dummy_node)

if __name__ == "__main__":
    main()