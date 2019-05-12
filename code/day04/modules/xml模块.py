
from xml.etree import ElementTree as ET

### 创建一个xml文件
def build_sitemap():
    urlset = ET.Element("urlset") #创建根节点标签为 urlset
    url = ET.SubElement(urlset,"url",attrib={"isinstance":"true"}) #在根节点urlset下创建子节点
    loc = ET.SubElement(url,"loc")
    loc.text = "http://www.baidu.com"
    lastmod = ET.SubElement(url,"lastmod")
    lastmod.text = "2019/4/12"
    changefreq = ET.SubElement(url,"changefreq")
    changefreq.text = "daily"
    priority = ET.SubElement(url, "priority")
    priority.text = "1.0"
    tree = ET.ElementTree(urlset) #ElementTree(tag)，其中tag表示根节点，初始化一个ElementTree对象。
    tree.write("sitmap.xml")
    # ElementTree.write(file, encoding='us-ascii', xml_declaration=None,
    # default_namespace=None, method='xml')，函数新建一个XML文件，并且将节点数数据写入XML文件中


if __name__ == '__main__':
    build_sitemap()

