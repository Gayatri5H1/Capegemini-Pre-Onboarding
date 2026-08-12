import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    ct = 0
    for ele in node.iter():
        ct += len(ele.attrib)
    return ct

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
