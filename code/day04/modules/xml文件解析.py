
from xml.etree import ElementTree as ET

tree = ET.parse("sitmap.xml") # ElementTree.parse(source, parser=None)，将xml文件加载并返回ElementTree对象。
url = tree.find("url")

for rank in tree.iter('loc'):  # 创建一个以当前节点为根节点的iterator。
    rank.text = "http://www.adminba.com"
    rank.attrib = {"enable":"true"}
tree.write("sitemap.xml")