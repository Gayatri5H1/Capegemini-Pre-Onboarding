from html.parser import HTMLParser
class Main(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)
parser = Main()
for _ in range(int(input())):
    parser.feed(input())
