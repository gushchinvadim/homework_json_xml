from collections import Counter 
import xml.etree.ElementTree as ET
def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding= 'utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    file_path = root.findall("channel/item/description")
    popular = []

    for word in file_path:
          x = (word['description'].split(' '))
          name = [i for i in x if len(i) > word_max_len]
          popular.extend(name)
          words_counter = Counter(popular)
          top_10 = [w[0] for w in words_counter.most_common(top_words_amt)]

    return top_10


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))

