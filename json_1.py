import json
from collections import Counter
def read_json(file_path, word_max_len=6, top_words_amt=10):
   
        with open("newsafr.json", 'r') as f:
         json_file = json.load(f)
         popular = []
         file_path = json_file['rss']['channel']['items']  
        for word in file_path:
          x = (word['description'].split(' '))
          name = [i for i in x if len(i) > word_max_len]
          popular.extend(name)
          words_counter = Counter(popular)
          top_10 = [w[0] for w in words_counter.most_common(top_words_amt)]
        return top_10

if __name__ == '__main__':
    print(read_json('newsafr.json'))