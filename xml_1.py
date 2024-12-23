def read_xml(file_path, word_max_len=6, top_words_amt=10):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding= 'utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    news_list = root.findall("channel/item/description")
    description_words = []
    for news in news_list:
        result = news.text()
    description_words.append(result)
    return description_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))

