import xml.etree.ElementTree as ET
from collections import Counter
def read_xml(file, len_word=6, top_words=10):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    new_list = root.findall("channel/item")
    description = new_list[0].find("description")
    popular = []
    for row in new_list:    
        x = row.find("description").text.split(' ')
        name = [i for i in x if len(i) > len_word]
        popular.extend(name)
        words_counter = Counter(popular)
        top_10 = [w[0] for w in words_counter.most_common(top_words)]
    return top_10
if __name__ == '__main__':
    print(read_xml('newsafr.xml'))